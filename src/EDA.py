#%%
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
import seaborn as sns

#%%

with open('query3.sql', 'r') as f:
   query = f.read()
   
engine = sqlalchemy.create_engine('sqlite:///../data/database_tse.db')

df = pd.read_sql(query, engine)

df.head()



# %%
with open('query_tb_candidaturas.sql', 'r') as f:
   query2 = f.read()

df_candidates = pd.read_sql(query2, engine)
df_candidates.head()



# %%
with open('query_ipatinga.sql', 'r') as f:
   query3 = f.read()

df_ipatinga = pd.read_sql(query3, engine)
df_ipatinga.head()


# %%
df_ipatinga['SQ_CANDIDATO'].nunique()

#%%
df_ipatinga['SG_PARTIDO'].value_counts().plot(kind='pie', autopct='%1.1f%%')
# %%
df_ipatinga['DS_GRAU_INSTRUCAO'].value_counts().plot(kind='pie', autopct='%1.1f%%')
# %%

df_ipatinga['DS_GENERO'].value_counts().plot(kind='pie', autopct='%1.1f%%')

# %%
df_ipatinga['DS_COR_RACA'].value_counts().plot(kind='pie', autopct='%1.1f%%')

# %%
sns.boxplot(data=df_ipatinga['totalBens'].drop(352))
# %%
df_ipatinga[df_ipatinga['totalBens'] == df_ipatinga['totalBens'].max()]
# %%
df_ipatinga.loc[352]
# %%
sns.kdeplot(data=df_ipatinga['totalBens'].drop(352))

# %%
df_ipatinga['totalBens']

# %%
