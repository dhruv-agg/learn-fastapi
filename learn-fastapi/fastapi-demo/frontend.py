import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Patient Management System")

# Home Page
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page",
    [
        "Home",
        "About",
        "View Patients",
        "View Patient by ID",
        "Create Patient",
        "Update Patient",
        "Delete Patient",
        "Sort Patients",
    ],
)

if page == "Home":
    st.header("Welcome to the Patient Management System")
    response = requests.get(f"{BASE_URL}/")
    st.write(response.json())

if page == "About":
    st.header("About the Patient Management System")
    response = requests.get(f"{BASE_URL}/about")
    st.write(response.json())

elif page == "View Patients":
    st.header("View All Patients")
    response = requests.get(f"{BASE_URL}/view")
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("Failed to fetch patients.")

elif page == "View Patient by ID":
    st.header("View Patient by ID")
    patient_id = st.text_input("Enter Patient ID:")
    if st.button("Fetch Patient"):
        response = requests.get(f"{BASE_URL}/patient/{patient_id}")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error(response.json()["detail"])

elif page == "Create Patient":
    st.header("Create a New Patient")
    patient_id = st.text_input("Patient ID:")
    name = st.text_input("Name:")
    city = st.text_input("City:")
    age = st.number_input("Age:", min_value=0)
    gender = st.selectbox(
        "Select your gender:", ["Male", "Female", "Other", "Prefer not to say"]
    )
    height = st.number_input("Height (m):", value=0.0, step=0.1, min_value=0.0)
    weight = st.number_input("Weight (kg):", value=0.0, step=0.1, min_value=0.0)

    if st.button("Create Patient"):
        payload = {
            "id": patient_id,
            "name": name,
            "city": city,
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight,
        }
        response = requests.post(f"{BASE_URL}/create", json=payload)
        if response.status_code == 201:
            st.success(response.json()["message"])
        else:
            st.error(response.json()["detail"])

elif page == "Update Patient":
    st.header("Update Patient Details")
    patient_id = st.text_input("Patient ID:")
    name = st.text_input("Name (optional):")
    city = st.text_input("City(optional):")
    age = st.number_input("Age(optional):", min_value=0)
    gender = st.selectbox(
        "Select your gender:", ["Male", "Female", "Other", "Prefer not to say"]
    )
    height = st.number_input("Height (m):", value=0.0, step=0.1, min_value=0.0)
    weight = st.number_input(
        "Weight (optional, kg):", value=0.0, step=0.1, min_value=0.0
    )
    if st.button("Update Patient"):
        payload = {
            "name": name if name else None,
            "city": city if city else None,
            "age": age if age else None,
            "gender": gender if gender else None,
            "height": height if height else None,
            "weight": weight if weight else None,
        }
        response = requests.put(f"{BASE_URL}/edit/{patient_id}", json=payload)

        # Check if the response contains valid JSON
        try:
            response_data = response.json()
            if response.status_code == 200:
                st.success(response_data.get("message", "Patient updated successfully"))
            else:
                st.error(f"Error: {response.status_code}")
                st.write("Response content:", response.text)
        except requests.exceptions.JSONDecodeError:
            st.error("Invalid response from the server.")

elif page == "Delete Patient":
    st.header("Delete a Patient")
    patient_id = st.text_input("Enter Patient ID:")
    if st.button("Delete Patient"):
        response = requests.delete(f"{BASE_URL}/delete/{patient_id}")
        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error(response.json()["detail"])

elif page == "Sort Patients":
    st.header("Sort Patients")
    sort_by = st.selectbox("Sort By:", ["height", "weight", "bmi"])
    order = st.selectbox("Order:", ["asc", "desc"])
    if st.button("Sort Patients"):
        response = requests.get(
            f"{BASE_URL}/sort", params={"sort_by": sort_by, "order": order}
        )
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error(response.json()["detail"])
