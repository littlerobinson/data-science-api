from app.models.group_by_model import GroupBy

import pandas as pd


async def sample(count: int):
    """
    Asynchronous function to sample a specified number of rows from the Excel file.

    Args:
        count (int): The number of rows to sample.

    Returns:
        pd.DataFrame: A DataFrame containing the sampled rows.
    """
    df = pd.read_excel("data/hr_attritions.xlsx")
    sample = df.sample(count)
    return sample


async def unique_values(column: str):
    """
    Asynchronous function to get unique values from a specified column in the Excel file.

    Args:
        column (str): The name of the column to retrieve unique values from.

    Returns:
        pd.Series: A Series containing the unique values from the specified column, or False if the column does not exist.
    """
    df = pd.read_excel("data/hr_attritions.xlsx")
    # Check if column exist
    if column not in df:
        return False

    return pd.Series(df[column].unique())


async def groupby(groupBy: GroupBy):
    """
    Asynchronous function to group data by a specified column and apply an aggregation method.

    Args:
        groupBy (GroupBy): An instance of GroupBy containing the method, column, and target_column.

    Returns:
        pd.DataFrame: A DataFrame containing the grouped and aggregated data.
    """
    df = pd.read_excel("data/hr_attritions.xlsx")

    method = groupBy.method
    column = groupBy.column
    target_column = groupBy.target_column

    if method == "mean":
        df = df.groupby(column)[target_column].mean().reset_index()
    if method == "median":
        df = df.groupby(column)[target_column].median().reset_index()
    if method == "min":
        df = df.groupby(column)[target_column].min().reset_index()
    if method == "max":
        df = df.groupby(column)[target_column].max().reset_index()
    if method == "sum":
        df = df.groupby(column)[target_column].sum().reset_index()
    if method == "count":
        df = df.groupby(column)[target_column].count().reset_index()

    df.columns = [column, target_column]

    return df


async def quantile(column: str, percent: float = 0.1, top: bool = True):
    """
    Asynchronous function to get quantile values from a specified column in the Excel file.

    Args:
        column (str): The name of the column to retrieve quantile values from.
        percent (float, optional): The percentile value. Defaults to 0.1.
        top (bool, optional): If True, retrieve values above the quantile; if False, retrieve values below the quantile. Defaults to True.

    Returns:
        pd.Series: A Series containing the unique quantile values from the specified column, or False if the percent value is out of range.
    """
    df = pd.read_excel("data/hr_attritions.xlsx")

    if percent > 0.99 or percent < 0.01:
        return False
    else:
        if top:
            data_quantile = df[df[column] > df[column].quantile(1 - percent)]
        else:
            data_quantile = df[df[column] < df[column].quantile(percent)]

        return pd.Series(data_quantile[column].unique())
