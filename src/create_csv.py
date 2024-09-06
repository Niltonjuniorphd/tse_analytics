import pandas as pd
import sqlalchemy


con = sqlalchemy.create_engine('sqlite:///../data/database_tse.db')
with open('query_ipatinga.sql', 'r') as f:
    query = f.read()

df_ipatinga = pd.read_sql(query, con)

df_ipatinga.to_csv('ipatinga.csv')