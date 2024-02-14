from datetime import datetime
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    df = data

    df['lpep_pickup_date'] = df['lpep_pickup_datetime'] .astype(str).apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').date())
    df['lpep_dropoff_date'] = df['lpep_dropoff_datetime'].astype(str).apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S').date())

    print(df.dtypes)

    return df


# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
