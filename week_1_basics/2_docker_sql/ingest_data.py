import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os


def main(params):
    
    user = params.user
    password = params.password
    host= params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'
    
    #download the csv #-0 specifies the output so wget to download from the url and write the result to a file with the name csv_name
    os.system(f"wget {url} -o {csv_name}")
    
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    #we want to split the data into chunks because we dont want to insert 1million rows into the 
    #database at once since we dont know how the database will react
    col_names = ['VendorID',
                'tpep_pickup_datetime',
                'tpep_dropoff_datetime',
                'passenger_count',
                'trip_distance',
                'RatecodeID',
                'store_and_fwd_flag',
                'PULocationID',
                'DOLocationID',
                'payment_type',
                'fare_amount',
                'extra',
                'mta_tax',
                'tip_amount',
                'improvement_surcharge',
                'total_amount',
                'congestion_surcharge']
    df_iter = pd.read_csv(csv_name, names=col_names, iterator=True, chunksize=100000)


    df = next(df_iter)

    #we only want to insert column names first, hence we use .head(n=0) to get the header. we will then insert data chunk by chunk
    #if_exists = if the table named table_name exists, it will replace it. 
    #to_sql inserts data into the database when using with con(connection)
    df.head(n=0).to_sql(table_name, con=engine, if_exists='replace') 

    #append, if exists, it will insert new values into the table. %time will tell us how long it took to run this command
    df.to_sql(table_name, con=engine, if_exists='append')

    #we will make an infinite loop to insert the chunks of data 1 by 1 until there is no more data left. 
    #when there is no more data left, it will throw an exception
    #.3f notation will treat the resulting value as a float and will have 3 decimal places. 
    while True:
        t_start = time()
        df=next(df_iter)
        
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        num_cols = ['VendorID','passenger_count','RatecodeID','PULocationID','DOLocationID','payment_type']
        flo_cols = ['trip_distance','fare_amount','extra','mta_tax','tip_amount','tolls_amount','improvement_surcharge','total_amount','congestion_surcharge']

        df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce').astype('Int64')
        df[flo_cols] = df[flo_cols].apply(pd.to_numeric, errors='coerce')


        df.to_sql(table_name, con=engine, if_exists='append')

        t_end = time()

        print('inserted another chunk... took %.3f seconds' % (t_end-t_start))

if __name__ == '__main__':
    

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()

    main(args)
