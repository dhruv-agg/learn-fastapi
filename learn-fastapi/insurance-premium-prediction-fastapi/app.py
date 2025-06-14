from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION

app = FastAPI()

@app.get("/")
def home():
    """
    Root endpoint to display a welcome message for the API.

    Returns:
        dict: A welcome message.
    """
    return {"message": "Insurance Premium Prediction API"}

@app.get("/health")
def health_check():
    """
    Endpoint to check the health of the API and model.

    Returns:
        dict: Health status, model version, and whether the model is loaded.
    """
    return {"status": "OK", "version": MODEL_VERSION, "model_loaded": model is not None}

@app.post("/predict", response_model=PredictionResponse)
def predict_premium(data: UserInput):
    """
    Endpoint to predict insurance premium based on user input.

    Args:
        data (UserInput): The user input data containing features like BMI, age group, lifestyle risk, etc.

    Returns:
        JSONResponse: A JSON response containing the predicted premium amount.

    Raises:
        JSONResponse: A JSON response with status code 500 if an exception occurs during prediction.
    """
    user_input = {
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation,
    }

    try:
        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={"response": prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))