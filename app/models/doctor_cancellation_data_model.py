from pydantic import BaseModel
from typing import Literal


class DoctorCancellationData(BaseModel):
    Gender: Literal["F", "M"]
    Age: float
    Neighbourhood: str
    Scholarship: float
    Hypertension: float
    Diabetes: float
    Alcoholism: float
    Handcap: float
    SMS_received: float
    diff_appointment_scheduled: float
    AppointmentDay_DayOfWeek: int
    AppointmentDay_Month: int
