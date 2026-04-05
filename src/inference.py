# Import Path so we can safely work with file and folder paths
from pathlib import Path

# Import YOLO from ultralytics to load and run the trained model
from ultralytics import YOLO

# Import settings from config.py
from config import MODEL_PATH, PREDICT_OUTPUT_DIR, CONFIDENCE_THRESHOLD, IMAGE_SIZE


def load_model(model_path=MODEL_PATH):
    """
    Load the trained YOLO model from the given path.
    
    Parameters:
        model_path: path to the trained model file (.pt)

    Returns:
        model: loaded YOLO model
    """

    # Check whether the model file actually exists
    if not Path(model_path).exists():
        # If the model file is missing, raise an error
        raise FileNotFoundError(f"Model not found at: {model_path}")

    # Load the YOLO model using the given path
    model = YOLO(str(model_path))

    # Return the loaded model so we can use it later
    return model


def predict_on_source(
    model,
    source,
    conf=CONFIDENCE_THRESHOLD,
    imgsz=IMAGE_SIZE,
    save=True,
    project=PREDICT_OUTPUT_DIR.parent,
    name="predict"
):
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

    # Run prediction using the YOLO model
    results = model.predict(
        source=str(source),   # Convert source path to string
        conf=conf,            # Set confidence threshold
        imgsz=imgsz,          # Set image size
        save=save,            # Save output images if True
        project=str(project), # Main output folder
        name=name,            # Subfolder name for this prediction run
        exist_ok=True         # If folder already exists, do not give error
    )

    # Return prediction results
    return results