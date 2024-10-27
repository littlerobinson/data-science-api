from fastapi import APIRouter, HTTPException, Response

import app.handlers.doctor_cancellation_detector_handler as hah
from app.models.doctor_cancellation_data_model import DoctorCancellationData
from app.models.group_by_model import GroupBy

import json


router = APIRouter(
    prefix="/doctor-cancellation-detector",
    # tags=["doctor-cancellation-detector"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    """
    Root endpoint to check the status of the doctor-cancellation-detector API.

    Returns:
        dict: A message indicating the API is working.
    """
    return {"message": "Hello Doctor Cancellation Detector"}


@router.get("/sample", tags=["data"])
async def sample(count: int = 10):
    """
    Endpoint to get a sample of rows from the Doctor Cancellation Detector data.

    Args:
        count (int, optional): The number of rows to sample. Defaults to 10.

    Returns:
        Response: A JSON response containing the sampled rows.
    """
    response = await hah.sample(count)
    return Response(response.to_json(orient="records"), media_type="application/json")


@router.get("/unique-values", tags=["data"])
async def unique_values(column: str):
    """
    Endpoint to get unique values from a specified column in the Doctor Cancellation Detector data.

    Args:
        column (str): The name of the column to retrieve unique values from.

    Returns:
        Response: A JSON response containing the unique values from the specified column.

    Raises:
        HTTPException: If the column does not exist.
    """
    response = await hah.unique_values(column)
    if response is False:
        raise HTTPException(status_code=404, detail="Item not found")
    return Response(response.to_json(orient="records"), media_type="application/json")


@router.post("/groupby", tags=["data"])
async def groupby(groupBy: GroupBy):
    """
    Endpoint to group data by a specified column and apply an aggregation method.

    Args:
        groupBy (GroupBy): An instance of GroupBy containing the method *, column, and target_column.

    Returns:
        Response: A JSON response containing the grouped and aggregated data.https://mlflow.luciole.dev/


    Available methods:
    * `mean`
    * `median`
    * `min`
    * `max`
    * `sum`
    * `count`
    """
    response = await hah.groupby(groupBy)
    return Response(response.to_json(orient="records"), media_type="application/json")


@router.get("/quantile", tags=["data"])
async def quantile(column: str, percent: float = 0.1, top: bool = True):
    """
    Endpoint to get quantile values from a specified column in the Doctor Cancellation Detector data.

    Args:
        column (str): The name of the column to retrieve quantile values from.
        percent (float, optional): The percentile value. Defaults to 0.1. *
        top (bool, optional): If True, retrieve values above the quantile; if False, retrieve values below the quantile. Defaults to True.

    Returns:
        Response: A JSON response containing the unique quantile values from the specified column.

    Raises:
        HTTPException: If the percent value is out of range or if the column does not exist.


    * Note: percent must between 0.01 to 0.99
    """
    response = await hah.quantile(column, percent, top)
    if response is False:
        raise HTTPException(
            status_code=404,
            detail="On error occur, check percent value and data type of the column",
        )
    return Response(response.to_json(orient="records"), media_type="application/json")


@router.post("/predict", tags=["machine-learning"])
async def predict(data: DoctorCancellationData):
    response = await hah.predict(data)
    return Response(content=json.dumps(response), media_type="application/json")
