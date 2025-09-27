from pydantic import BaseModel

class PatientData(BaseModel):
    first_name: str
    last_name: str
    identification_number: str
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

