import sys

from pathlib import Path

# Add the src folder to the Python module search path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))
from ultralytics import YOLO
from src.config import MODEL_PATH, PREDICT_OUTPUT_DIR, CONFIDENCE_THRESHOLD, IMAGE_SIZE
from fastapi import UploadFile
import shutil

def load_model(model_path=MODEL_PATH):
    """
    Load the trained YOLO model from the given path.
    
    Parameters:
        model_path: path to the trained model file (.pt)

    Returns:
        model: loaded YOLO model
    """
    if not Path(model_path).exists():
        raise FileNotFoundError(f"Model not found at: {model_path}")

    model = YOLO(str(model_path))
    return model


def predict_on_source(model, source, conf=CONFIDENCE_THRESHOLD, imgsz=IMAGE_SIZE, save=True, project=PREDICT_OUTPUT_DIR.parent, name="predict"):
    """
    Run prediction using the loaded model on the given source.
    
    Parameters:
        model   : loaded YOLO model
        source  : image path, folder path, video path, or webcam
        conf    : confidence threshold for predictions
        imgsz   : image size used during prediction
        save    : whether to save the prediction results
        project : main output folder
        name    : subfolder name inside the output folder

    Returns:
        results : prediction results from YOLO
    """
    results = model.predict(
        source=str(source),
        conf=conf,
        imgsz=imgsz,
        save=save,
        project=str(project),
        name=name,
        exist_ok=True
    )
    return results

def save_uploaded_file(upload_file: UploadFile):
    """
    Saves the uploaded file to the filesystem
    """
    file_path = f"temp_{upload_file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return file_path