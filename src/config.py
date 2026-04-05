from pathlib import Path

# --------------------------------------------------
# Project Root
# --------------------------------------------------
# This file is inside: src/config.py
# So project root = one level above "src"
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# Dataset Paths
# --------------------------------------------------
DATA_DIR = BASE_DIR / "data"
DATA_YAML = DATA_DIR / "data.yaml"

TRAIN_IMAGES_DIR = DATA_DIR / "train" / "images"
VALID_IMAGES_DIR = DATA_DIR / "valid" / "images"
TEST_IMAGES_DIR = DATA_DIR / "test" / "images"

# --------------------------------------------------
# Model Paths
# --------------------------------------------------
# Trained YOLO model after training
MODEL_PATH = BASE_DIR / "models" / "best.pt"



# --------------------------------------------------
# Output Paths
# --------------------------------------------------
OUTPUTS_DIR = BASE_DIR / "outputs"
PREDICT_OUTPUT_DIR = OUTPUTS_DIR / "predictions"

# --------------------------------------------------
# Inference Settings
# --------------------------------------------------
CONFIDENCE_THRESHOLD = 0.25
IOU_THRESHOLD = 0.45
IMAGE_SIZE = 640

# --------------------------------------------------
# Class Names
# --------------------------------------------------
CLASS_NAMES = [
    "missing_hole",
    "mouse_bite",
    "open_circuit",
    "short",
    "spur",
    "spurious_copper",
]

# --------------------------------------------------
# Visualization Settings
# --------------------------------------------------
LINE_WIDTH = 2
FONT_SCALE = 0.5
FONT_THICKNESS = 1

# --------------------------------------------------
# Supported File Extensions
# --------------------------------------------------
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

# --------------------------------------------------
# Create Important Folders Automatically
# --------------------------------------------------
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
PREDICT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)