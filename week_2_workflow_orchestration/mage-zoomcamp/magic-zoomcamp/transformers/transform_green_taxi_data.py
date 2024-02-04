import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # remove rows with passenger_count = 0 or trip_distance = 0
    df = data[(data["passenger_count"]>0) & (data["trip_distance"]>0)]

    # create new column lpep_pickup_date by converting lpep_pickup_datetime to a date
    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date
    print(df.dtypes)

    #rename columns in camel case to snake case
    df.columns = (df.columns
                    .str.replace('ID','_ID')
                    .str.replace('Location','_Location')
                    .str.lower()
                )

    print(df.dtypes)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert 'vendor_id' in output.columns, "There is no column named 'vendor_id'"
    assert output["passenger_count"].isin([0]).sum() == 0, 'There are rides with zero passengers'
    assert output["trip_distance"].isin([0]).sum() == 0, 'There are rides with zero trip distance'
