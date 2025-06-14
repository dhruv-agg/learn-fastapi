# Patient Management System API

This project is a FastAPI-based application for managing patient records. It provides endpoints to create, view, update, delete, and sort patient data. The application uses Pydantic models for data validation and JSON files for data storage.

## Features

- **View All Patients**: Retrieve all patient records.
- **View Patient by ID**: Fetch details of a specific patient.
- **Create Patient**: Add a new patient to the database.
- **Update Patient**: Modify existing patient details.
- **Delete Patient**: Remove a patient from the database.
- **Sort Patients**: Sort patient records by height, weight, or BMI.

## Prerequisites

- Python 3.10 or higher installed on your system.
- `uv` package manager installed.

## Setup Instructions

Follow these steps to set up and run the project locally:

### 1. Install the `uv` Package Manager
```bash
pip install uv
```

### 2. Create a Virtual Environment
```bash
uv init
```

### 3. Add Required Dependencies
```bash
uv add fastapi uvicorn pydantic
```

### 4. Run the Application
Start the FastAPI application using Uvicorn:
```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### **GET** `/`
Returns a welcome message.

### **GET** `/about`
Provides information about the API.

### **GET** `/view`
Fetches all patient records.

### **GET** `/patient/{patient_id}`
Retrieves details of a specific patient by ID.

### **GET** `/sort`
Sorts patient records by height, weight, or BMI in ascending or descending order.

### **POST** `/create`
Creates a new patient record. Requires a JSON payload with patient details.

### **PUT** `/edit/{patient_id}`
Updates an existing patient record. Requires the patient ID and a JSON payload with updated details.

### **DELETE** `/delete/{patient_id}`
Deletes a patient record by ID.

## Example Usage

### Create a Patient
```bash
curl -X POST "http://127.0.0.1:8000/create" -H "Content-Type: application/json" -d '{
    "id": "P001",
    "name": "John Doe",
    "age": 30,
    "height": 180,
    "weight": 75
}'
```

### Update a Patient
```bash
curl -X PUT "http://127.0.0.1:8000/edit/P001" -H "Content-Type: application/json" -d '{
    "weight": 80
}'
```

### Delete a Patient
```bash
curl -X DELETE "http://127.0.0.1:8000/delete/P001"
```

### Run the Streamlit app
```bash
streamlit run main.py
```


## Project Structure

```
├── main.py                # FastAPI application
├── schema.py              # Pydantic models for validation
├── utils.py               # Utility functions for data handling
├── patients.json          # JSON file for storing patient data
├── README.md              # Project documentation
```

## License

This project is licensed under the MIT License.

## Contributing

Feel free to fork this repository and submit pull requests to improve the API or add new features.