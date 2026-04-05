# Import the folder path of test images from config.py
from config import TEST_IMAGES_DIR

# Import the functions we wrote in inference.py
from inference import load_model, predict_on_source


def main():
    """
    Main function of the project.
    This function will:
    1. Load the trained YOLO model
    2. Run prediction on the test images
    3. Print status messages in the terminal
    """

    # Print a message so we know the program has started
    print("Loading trained model...")

    # Load the trained YOLO model using the function from inference.py
    model = load_model()

    # Print a message before starting prediction
    print("Running prediction on test images...")

    # Run prediction on all images inside the test/images folder
    results = predict_on_source(
        model=model,              # the loaded YOLO model
        source=TEST_IMAGES_DIR,   # folder containing test images
        name="pcb_test_predictions"  # name of the output subfolder
    )

    # Print a success message after prediction is complete
    print("Prediction completed successfully.")

    # Tell the user where to check the output images
    print("Check the saved prediction results in the outputs folder.")

    # Return results if you want to use them later
    return results


# This makes sure the code runs only when this file is executed directly
if __name__ == "__main__":
    main()