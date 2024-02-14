import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    
    urls = [
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-01.parquet',
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-02.parquet',
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-03.parquet',
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-04.parquet',
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-05.parquet',
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-06.parquet',
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-07.parquet',
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-08.parquet',
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-09.parquet',
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-10.parquet',
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-11.parquet',
            'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-12.parquet'
            ]
    
    taxi_data = pd.concat(map(pd.read_parquet,urls))
    print(len(taxi_data))

    return taxi_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
