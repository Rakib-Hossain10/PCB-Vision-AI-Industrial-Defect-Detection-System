from fastapi import FastAPI, File, UploadFile
from backend.app.inference import load_model, predict_on_source, save_uploaded_file
from src.config import PREDICT_OUTPUT_DIR
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import base64
from io import BytesIO
import os

app = FastAPI()

# --------------------------------------------------
# CORS Configuration
# --------------------------------------------------
# Changed to 5173 to match your Vite frontend default port
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://pcb-vision-ai-industrial-defect-det.vercel.app", # REMOVE the trailing slash /
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model once when the server starts to save memory and time
model = load_model()

# --------------------------------------------------
# Endpoints
# --------------------------------------------------

@app.get("/")
async def root():
    """Simple check to see if the API is alive."""
    return {"message": "FastAPI server is running"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """
    1. Receives an image from React.
    2. Saves it locally.
    3. Runs YOLO inference.
    4. Returns the result image as a Base64 string.
    """
    
    # 1. Save the uploaded file 
    # This function returns the full path (e.g., ".../temp_1.jpg")
    image_path = save_uploaded_file(file)

    # Get the actual filename used on disk (e.g., "temp_1.jpg")
    # This is critical because it's what YOLO uses to name the output file
    saved_filename = os.path.basename(image_path)

    # 2. Run prediction on the saved temporary image
    # Note: 'results' is a list of Ultralytics result objects
    results = predict_on_source(
        model=model,
        source=image_path,
        save=True,
        project=PREDICT_OUTPUT_DIR.parent,
        name="predict_results"
    )

    # 3. Construct the path to the result image created by YOLO
    # We use 'saved_filename' instead of 'file.filename' to avoid Mismatch Errors
    result_image_path = os.path.join(PREDICT_OUTPUT_DIR.parent, "predict_results", saved_filename)
    
    # Safety Check: If for some reason YOLO didn't save the file, return an error instead of crashing
    if not os.path.exists(result_image_path):
        return {
            "message": "Prediction failed",
            "error": f"Result file not found at {result_image_path}"
        }

    # 4. Open the result image and convert it to Base64
    img = Image.open(result_image_path)
    
    # We use a Buffer to store the image bytes in memory
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    
    # Encode the bytes to base64 string for the React frontend
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    # 5. Clean up (Optional)
    # If you don't want to fill up your hard drive, uncomment the line below:
    # os.remove(image_path) 

    return {
        "message": "Prediction completed successfully",
        # We don't return the raw 'results' object directly as it contains complex 
        # Tensors that aren't JSON serializable. The Base64 image is what we need.
        "image_with_bounding_boxes": img_base64 
    }