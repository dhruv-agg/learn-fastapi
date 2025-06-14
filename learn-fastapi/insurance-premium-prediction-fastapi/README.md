# Insurance Premium Prediction API

This project is a FastAPI-based application that predicts insurance premium categories based on user input. It uses a machine learning model to classify users into premium categories based on features such as age, BMI, income, lifestyle risk, and more. A Streamlit frontend is provided for easy interaction with the API.

---

## Features

### **API Endpoints**
1. **`GET /`**: Root endpoint to display a welcome message.
2. **`GET /health`**: Check the health status of the API and model.
3. **`POST /predict`**: Predict insurance premium categories based on user input.

### **Streamlit Frontend**
- **Home Page**: Displays a welcome message and instructions.
- **Health Page**: Checks the API and model status.
- **Predict Page**: Allows users to input their details and get predictions.

---

## Prerequisites

- Python 3.10 or higher installed on your system.
- `uv` package manager installed for backend setup.
- `Streamlit` installed for frontend interaction.

---

## Setup Instructions

### **Backend Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/insurance-premium-prediction-fastapi.git
   cd insurance-premium-prediction-fastapi
   ```

2. Install the `uv` package manager:
   ```bash
   pip install uv
   ```

3. Create a virtual environment:
   ```bash
   uv venv
   ```

4. Add required dependencies:
   ```bash
   uv add fastapi uvicorn pydantic scikit-learn
   ```

5. Run the FastAPI backend:
   ```bash
   uvicorn app:app --reload
   ```

The backend will be available at `http://127.0.0.1:8000`.

---

### **Frontend Setup**
1. Install Streamlit:
   ```bash
   pip install streamlit
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run frontend.py
   ```

The frontend will be available at `http://localhost:8501`.

---

## Example Usage

### **Predict Insurance Premium**
1. Navigate to the **Predict** page in the Streamlit app.
2. Enter your details:
   - Age
   - Weight
   - Height
   - Annual Income (LPA)
   - Smoker status
   - City
   - Occupation
3. Click **Predict Premium Category** to get the prediction.

---

## Project Structure

```
├── app.py                     # FastAPI backend
├── frontend.py                # Streamlit frontend
├── schema/                    # Pydantic models for validation
│   ├── user_input.py          # User input schema
│   ├── prediction_response.py # Prediction response schema
├── model/                     # Machine learning model logic
│   ├── predict.py             # Prediction logic
├── README.md                  # Project documentation
```

---

## API Documentation

### **Health Check**
```bash
curl -X GET "http://127.0.0.1:8000/health"
```

### **Predict Premium**
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{
    "age": 30,
    "weight": 65,
    "height": 1.7,
    "income_lpa": 10,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
}'
```

---

## License

This project is licensed under the MIT License.

---

## Contributing

Feel free to fork this repository and submit pull requests to improve the API or add new features.