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


path = r'C:\Users\Besitzer\Desktop\projects\Github_Repositories\cfa_binance\data\raw'
path2 = r'C:\Users\Besitzer\Desktop\projects\Github_Repositories\cfa_binance\data\proceed'

df_assets  = pd.read_csv(f"{path}/assets.csv")
df_hourly = pd.read_csv(f"{path}/All_2017_01_01_to_2023_07_06_hourly.csv")
df_daily = pd.read_csv(f"{path}/All_2017_01_01_to_2023_07_06_daily.csv")
df_weekly = pd.read_csv(f"{path}/All_2017_01_01_to_2023_07_06_weekly.csv")
df_monthly = pd.read_csv(f"{path}/All_2017_01_01_to_2023_07_06_monthly.csv")
df_procedd_all = pd.read_csv(f"{path2}/daily_proceed_all.csv")

print(f'{df_hourly} , {df_daily}, {df_weekly}, {df_monthly}, {df_procedd_all} loaded.')

table_name_list = ['assets', 'hourly','daily','weekly','monthly', 'daily_proceed_all'  ]
df_list = [df_assets, df_hourly, df_daily, df_weekly, df_monthly, df_procedd_all]

#  Note:  if_exists can be append, replace, fail.  
for df, table_name in zip(df_list, table_name_list):
    df.to_sql(f'{table_name}', engine, if_exists='append', index = False)
    print(f'{table_name} tables data added to database.')

sql_update_id = ''' UPDATE daily_proceed_all
                    SET id = daily.id
                    FROM daily
                    WHERE daily_proceed_all.timestamp = daily.timestamp
                    AND daily_proceed_all.id_asset = daily.id_asset
                    AND daily_proceed_all.close = daily.close; '''

cursor.execute(sql_update_id)