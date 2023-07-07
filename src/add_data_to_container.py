# import libraries
import pandas as pd
import psycopg2
from sqlalchemy import create_engine,select, insert

conn = psycopg2.connect(database="binance",
			user='abdullahcay', password=12345,
			host='127.0.0.1', port='5434'
)

conn.autocommit = True
cursor = conn.cursor()

db_string = "postgresql://abdullahcay:12345@localhost:5434/binance"
engine = create_engine(db_string)

df_assets = pd.DataFrame({'id_asset' : [1,2,3],
                         'name' : ['BTCUSDT', 'ETHBTC', 'ETHUSDT']})
print(df_assets)

table_name_list = ['hourly','daily','weekly','monthly']

table_name = 'assets'
df_assets.to_sql(f'{table_name}', engine, if_exists='append', index = False)
print(f'{table_name} table added to database.')

path = '/Users/macbook/Desktop/projects/Github_Repositories/cfa_binance/data/raw'
df_hourly = pd.read_csv(f'{path}/All_2017_01_01_to_2023_07_06_hourly.csv')
df_daily = pd.read_csv(f'{path}/All_2017_01_01_to_2023_07_06_daily.csv')
df_weekly = pd.read_csv(f'{path}/All_2017_01_01_to_2023_07_06_weekly.csv')
df_monthly = pd.read_csv(f'{path}/All_2017_01_01_to_2023_07_06_monthly.csv')
print(df_daily.tail())

table_name_list = ['hourly','daily','weekly','monthly']
df_list = [df_hourly, df_daily, df_weekly, df_monthly]

#  Note:  if_exists can be append, replace, fail.  
for df, table_name in zip(df_list, table_name_list):
    df.to_sql(f'{table_name}', engine, if_exists='append', index = False)
    print(f'{table_name} table added to database.')
