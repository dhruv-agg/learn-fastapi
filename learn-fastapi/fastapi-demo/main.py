from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from utils import load_data, save_data
from schema import Patient, PatientUpdate
import logging

logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/")
def hello():
    """
    Root endpoint to display a welcome message for the API.

    Returns:
        dict: A welcome message.
    """
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    """
    Endpoint to provide information about the API.

    Returns:
        dict: Information about the API.
    """
    return {"message": "A fully functional API to manage your patient records"}


@app.get("/view")
def view():
    """
    Endpoint to fetch all patient records from the database.

    Returns:
        dict: All patient records.
    """
    data = load_data()
    return data


@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ..., description="ID of the patient in the DB", examples="P001"
    ),
):
    """
    Endpoint to fetch details of a specific patient by their ID.

    Args:
        patient_id (str): The ID of the patient.

    Returns:
        dict: Patient details if found.

    Raises:
        HTTPException: If the patient is not found.
    """
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


@app.post("/create")
def create_patient(patient: Patient):
    """
    Endpoint to create a new patient record.

    Args:
        patient (Patient): The patient data to be added.

    Returns:
        JSONResponse: Success message if the patient is created.

    Raises:
        HTTPException: If the patient already exists.
    """
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    # Add the new patient to the database
    data[patient.id] = patient.model_dump(exclude=["id"])

    # Save the updated data to the JSON file
    save_data(data)

    return JSONResponse(
        status_code=201, content={"message": "patient created successfully"}
    )


@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient_update: PatientUpdate):
    """
    Endpoint to update an existing patient's details.

    Args:
        patient_id (str): The ID of the patient to be updated.
        patient_update (PatientUpdate): The updated patient data.

    Returns:
        JSONResponse: Success message if the patient is updated.

    Raises:
        HTTPException: If the patient is not found.
    """
    try:
        data = load_data()

        if patient_id not in data:
            raise HTTPException(status_code=404, detail="Patient not found")

        existing_patient_info = data[patient_id]

        # Update the patient details with the provided data
        updated_patient_info = patient_update.model_dump(exclude_unset=True)

        for key, value in updated_patient_info.items():
            existing_patient_info[key] = value

        # Convert the updated patient info to a Pydantic object for validation
        existing_patient_info["id"] = patient_id
        patient_pydandic_obj = Patient(**existing_patient_info)

        # Convert the Pydantic object back to a dictionary
        existing_patient_info = patient_pydandic_obj.model_dump(exclude="id")

        # Save the updated patient info to the database
        data[patient_id] = existing_patient_info
        save_data(data)

        return JSONResponse(status_code=200, content={"message": "patient updated"})
    except Exception as e:
        logger.error(f"Error updating patient: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    """
    Endpoint to delete a patient record by their ID.

    Args:
        patient_id (str): The ID of the patient to be deleted.

    Returns:
        JSONResponse: Success message if the patient is deleted.

    Raises:
        HTTPException: If the patient is not found.
    """
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Remove the patient from the database
    del data[patient_id]

    # Save the updated data to the JSON file
    save_data(data)

    return JSONResponse(status_code=200, content={"message": "patient deleted"})


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi"),
    order: str = Query("asc", description="sort in asc or desc order"),
):
    """
    Endpoint to sort patient records based on height, weight, or BMI.

    Args:
        sort_by (str): The field to sort by (height, weight, or bmi).
        order (str): The sort order (asc or desc).

    Returns:
        list: Sorted patient records.

    Raises:
        HTTPException: If the sort field or order is invalid.
    """
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400, detail=f"Invalid field select from {valid_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400, detail="Invalid order select between asc and desc"
        )

    data = load_data()

    # Determine the sort order (ascending or descending)
    sort_order = True if order == "desc" else False

    # Sort the data based on the specified field and order
    sorted_data = sorted(
        data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order
    )

    return sorted_data
