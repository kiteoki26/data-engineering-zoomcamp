import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/dtc-de-course-412407-fe7d84b57271.json'

bucket_name = 'de_zoomcamp_kim_teoh'
project_id = 'dtc-de-course-412407'
file_name = 'green_taxidata_2020'
root_path = f'{bucket_name}/{file_name}'


@data_exporter
def export_data(data, *args, **kwargs):
    
    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()
    
    pq.write_to_dataset(
        table,
        root_path = root_path,
        use_deprecated_int96_timestamps=True,
        filesystem=gcs,
    )


