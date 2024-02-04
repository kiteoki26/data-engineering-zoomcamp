import pandas as pd 
df=pd.read_csv('green_tripdata_2019-09.csv')
df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime).dt.date
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime).dt.date

df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)


#Q3
df[(df['lpep_pickup_datetime'] >= '2019-09-18') & (df['lpep_dropoff_datetime'] <= '2019-09-18')]

#Q4
df.groupby(['lpep_pickup_datetime'])['trip_distance'].agg('sum').sort_values(ascending=False).head(5)

#Q5
zones = pd.read_csv('taxi+_zone_lookup.csv')
joined_df = df.merge(zones, left_on='PULocationID', right_on='LocationID', how='left')
filt_df = joined_df[(joined_df['lpep_pickup_datetime']=='2019-09-18') & (joined_df['Borough']!='Unknown')]
filt_df2 = filt_df.groupby(['Borough']).agg({'total_amount':'sum'})


#Q6
zones2 = zones[['LocationID','Zone']]
zones2

pickup_df = df.merge(zones2,left_on='PULocationID',right_on='LocationID',how='left')
pickup_df = pickup_df.rename(columns={'Zone':'PickupZone'}).drop(['LocationID'],axis=1)

q6_df = pickup_df.merge(zones2,left_on='DOLocationID',right_on='LocationID',how='left')
q6_df = q6_df.rename(columns={'Zone':'DropoffZone'}).drop(['LocationID'],axis=1)
q6_df = q6_df.loc[q6_df["lpep_pickup_datetime"].between("2019-09-01", "2019-09-30")]
# For the passengers picked up in September 2019 in the zone name Astoria 
# which was the drop off zone that had the largest tip? We want the name of the zone, not the id.

df2 = q6_df[q6_df['PickupZone']=='Astoria']
df2.sort_values(by='tip_amount',ascending=False)

