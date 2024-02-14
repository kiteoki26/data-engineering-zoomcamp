-- create external table
CREATE OR REPLACE EXTERNAL TABLE `dtc-de-course-412407.ny_taxi.external_green_cab_data`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://de_zoomcamp_kim_teoh/green_taxidata_2020/376db07cce104a50b3c9f26b5da7b5a3-0.parquet']
);

-- create a materialized table
CREATE OR REPLACE TABLE dtc-de-course-412407.ny_taxi.green_cab_data AS
SELECT * FROM dtc-de-course-412407.ny_taxi.external_green_cab_data
;

-- Q1. 999,657
SELECT count(*) FROM dtc-de-course-412407.ny_taxi.external_green_cab_data
;

-- Q2. 0(External), 7.63(Materialized) in MB
SELECT DISTINCT PULocationID FROM dtc-de-course-412407.ny_taxi.external_green_cab_data; --0 MB
SELECT DISTINCT PULocationID FROM dtc-de-course-412407.ny_taxi.green_cab_data; --7.63MB

-- Q3. 2321
SELECT count(*) FROM dtc-de-course-412407.ny_taxi.external_green_cab_data
WHERE fare_amount = 0
;

-- Q4 Parition by lpep_pickup_datetime, Cluster by PULocationID
--create a partitioned table from external table
CREATE OR REPLACE TABLE dtc-de-course-412407.ny_taxi.green_cab_data_par_clus
PARTITION BY 
  DATE(lpep_pickup_datetime) 
CLUSTER BY 
  PULocationID AS
SELECT * FROM dtc-de-course-412407.ny_taxi.external_green_cab_data
;

--Q5. 15.25(Non-partitioned), 1.12(Partitioned) in MB
SELECT DISTINCT PULocationID FROM dtc-de-course-412407.ny_taxi.green_cab_data
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' and '2022-06-30';

SELECT DISTINCT PULocationID FROM dtc-de-course-412407.ny_taxi.green_cab_data_par_clus
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' and '2022-06-30';




