from pydantic import BaseModel
from typing import Literal, Union


class DoctorCancellationData(BaseModel):
    Gender: Literal["F", "M"]
    Age: Union[int, float]
    Neighbourhood: str
    Scholarship: Union[int, float]
    Hypertension: Union[int, float]
    Diabetes: Union[int, float]
    Alcoholism: Union[int, float]
    Handcap: Union[int, float]
    SMS_received: Union[int, float]
    diff_appointment_scheduled: Union[int, float]
    AppointmentDay_DayOfWeek: Union[int, float]
    AppointmentDay_Month: Union[int, float]
