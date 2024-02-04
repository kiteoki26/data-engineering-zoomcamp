if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data.columns = (data.columns
                    .str.replace(' ','_')
                    .str.lower()
    )
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    cols = output.columns
    uc_cols = []
    for c in cols:
        if c.islower():
            continue
        else:
            uc_cols.append(c)

    assert uc_cols is not None, 'There are column names that have uppercase characters'
