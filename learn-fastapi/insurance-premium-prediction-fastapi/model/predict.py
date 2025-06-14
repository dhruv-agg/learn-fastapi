import pickle
import pandas as pd

# Import the ML model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

# MLFlow
MODEL_VERSION = "1.0.0"

# Get class labels from model (important for matching probabilities to class names)
class_labels = model.classes_.tolist()


def predict_output(user_input: dict):
    """
    Predict the insurance premium category based on user input.

    Args:
        user_input (dict): A dictionary containing user features such as age, weight, height, income, smoker status, city, and occupation.

    Returns:
        dict: A dictionary containing:
            - predicted_category (str): The predicted insurance premium category.
            - confidence (float): The confidence score of the prediction.
            - class_probabilities (dict): A mapping of class names to their respective probabilities.
    """
    # Convert user input into a DataFrame
    df = pd.DataFrame([user_input])

    # Predict the class
    predicted_class = model.predict(df)[0]

    # Get probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    # Create mapping: {class_name: probability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs,
    }
