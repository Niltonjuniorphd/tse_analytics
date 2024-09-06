import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#
df_ipatinga = pd.read_csv('csv/ipatinga.csv')

df_ipatinga_filter = df_ipatinga[df_ipatinga['totalBens'] <= 1.5e7]

st.markdown("<h1 style='text-align: center; color: wite;'>TSE Analitics - Candidatos 2024</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: wite;'>Análise de dados do TSE para os candidatos de Ipatinga-MG</h4>", unsafe_allow_html=True)

st.text('')

#st.title('')
st.markdown("<h2 style='text-align: center; color: wite;'>Representatividade por partidos</h2>", unsafe_allow_html=True)
labels = df_ipatinga['SG_PARTIDO'].value_counts().index
sizes = df_ipatinga['SG_PARTIDO'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', #explode=explode, 
        shadow=False, startangle=90, textprops={'fontsize': 8})
ax1.axis('equal')# Equal aspect ratio ensures that pie is drawn as a circle.
#ax1.set_title('Grau de Instrução', fontsize=16, pad=20)
st.pyplot(fig1)
sizes

st.title('')
st.markdown("<h2 style='text-align: center; color: wite;'>Grau de ensino geral</h2>", unsafe_allow_html=True)
labels = df_ipatinga['DS_GRAU_INSTRUCAO'].value_counts().index
new_label = ('MÉDIO', 'SUPERIOR',
       'FUNDAMENTAL', 'FUNDAMENTAL IN',
       'SUPERIOR IN', 'MÉDIO IN', 'LÊ-ESCR')

sizes = df_ipatinga['DS_GRAU_INSTRUCAO'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=new_label, autopct='%1.1f%%', #explode=explode, 
        shadow=False, startangle=90, textprops={'fontsize': 8})
ax1.axis('equal')# Equal aspect ratio ensures that pie is drawn as a circle.
#ax1.set_title('Grau de Instrução', fontsize=16, pad=20)
st.pyplot(fig1)
sizes

ens_fem = df_ipatinga_filter[df_ipatinga_filter['DS_GENERO'] == 'FEMININO']

st.title('')
st.markdown("<h2 style='text-align: center; color: wite;'>Grau de ensino das Mulheres</h2>", unsafe_allow_html=True)
labels = ens_fem['DS_GRAU_INSTRUCAO'].value_counts().index
new_label = ('MÉDIO', 'SUPERIOR',
       'FUNDAMENTAL', 'FUNDAMENTAL IN',
       'SUPERIOR IN', 'MÉDIO IN', 'LÊ-ESCR')
sizes = ens_fem['DS_GRAU_INSTRUCAO'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=new_label, autopct='%1.1f%%', #explode=explode, 
        shadow=False, startangle=90, textprops={'fontsize': 8})
ax1.axis('equal')# Equal aspect ratio ensures that pie is drawn as a circle.
#ax1.set_title('Grau de Instrução', fontsize=16, pad=20)
st.pyplot(fig1)

ens_masc = df_ipatinga_filter[df_ipatinga_filter['DS_GENERO'] == 'MASCULINO']

st.title('')
st.markdown("<h2 style='text-align: center; color: wite;'>Grau de ensino dos Homens</h2>", unsafe_allow_html=True)
labels = ens_masc['DS_GRAU_INSTRUCAO'].value_counts().index
new_label = ('MÉDIO', 'SUPERIOR',
       'FUNDAMENTAL', 'FUNDAMENTAL IN',
       'SUPERIOR IN', 'MÉDIO IN', 'LÊ-ESCR')
sizes = ens_masc['DS_GRAU_INSTRUCAO'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=new_label, autopct='%1.1f%%', #explode=explode, 
        shadow=False, startangle=90, textprops={'fontsize': 8})
ax1.axis('equal')# Equal aspect ratio ensures that pie is drawn as a circle.
#ax1.set_title('Grau de Instrução', fontsize=16, pad=20)
st.pyplot(fig1)

st.title('')
st.markdown("<h2 style='text-align: center; color: wite;'>Gênero</h2>", unsafe_allow_html=True)
labels = df_ipatinga['DS_GENERO'].value_counts().index
sizes = df_ipatinga['DS_GENERO'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', #explode=explode, 
        shadow=False, startangle=90, textprops={'fontsize': 8})
ax1.axis('equal')# Equal aspect ratio ensures that pie is drawn as a circle.
#ax1.set_title('Grau de Instrução', fontsize=16, pad=20)
st.pyplot(fig1)
sizes

st.title('')
st.markdown("<h2 style='text-align: center; color: wite;'>Cor-Raça</h2>", unsafe_allow_html=True)
labels = df_ipatinga['DS_COR_RACA'].value_counts().index
sizes = df_ipatinga['DS_COR_RACA'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', #explode=explode, 
        shadow=False, startangle=90, textprops={'fontsize': 8})
ax1.axis('equal')# Equal aspect ratio ensures that pie is drawn as a circle.
#ax1.set_title('Grau de Instrução', fontsize=16, pad=20)
st.pyplot(fig1)
sizes




df_bem_cor = df_ipatinga_filter.groupby(['DS_COR_RACA'])['totalBens'].agg(['sum', 'count']).reset_index()
df_bem_cor['bemMedio'] = df_bem_cor['sum'] / df_bem_cor['count']


st.title('')
st.markdown("<h2 style='text-align: center; color: wite;'>Bens declarados por Cor-Raça</h2>", unsafe_allow_html=True)
labels = df_bem_cor['DS_COR_RACA']
sizes = df_bem_cor['bemMedio']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', #explode=explode, 
        shadow=False, startangle=90, textprops={'fontsize': 8})
ax1.axis('equal')# Equal aspect ratio ensures that pie is drawn as a circle.
#ax1.set_title('Grau de Instrução', fontsize=16, pad=20)
st.pyplot(fig1)
df_bem_cor
st.text('Bem declarado de cor Amarela:')
df_ipatinga_filter[df_ipatinga_filter['DS_COR_RACA'] == 'AMARELA']
st.text('Maior bem declarado negro:')
df_ipatinga_filter[(df_ipatinga_filter['DS_COR_RACA'] == 'PRETA') & 
                   (df_ipatinga_filter['totalBens'] == df_ipatinga_filter[df_ipatinga_filter['DS_COR_RACA'] == 'PRETA']['totalBens'].max())]
st.text('Maior bem declarado branco:')
df_ipatinga_filter[(df_ipatinga_filter['DS_COR_RACA'] == 'BRANCA') & 
                   (df_ipatinga_filter['totalBens'] == df_ipatinga_filter[df_ipatinga_filter['DS_COR_RACA'] == 'BRANCA']['totalBens'].max())]


df_bem_gen = df_ipatinga_filter.groupby(['DS_GENERO'])['totalBens'].agg(['sum', 'count']).reset_index()
df_bem_gen['bemMedio'] = df_bem_gen['sum'] / df_bem_gen['count']


st.title('')
st.markdown("<h2 style='text-align: center; color: wite;'>Bens declarados por Gênero</h2>", unsafe_allow_html=True)
labels = df_bem_gen['DS_GENERO']
sizes = df_bem_gen['bemMedio']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', #explode=explode, 
        shadow=False, startangle=90, textprops={'fontsize': 8})
ax1.axis('equal')# Equal aspect ratio ensures that pie is drawn as a circle.
#ax1.set_title('Grau de Instrução', fontsize=16, pad=20)
st.pyplot(fig1)
df_bem_gen
st.text('Maior bem declarado feminino')
df_ipatinga_filter[(df_ipatinga_filter['DS_GENERO'] == 'FEMININO') & 
                   (df_ipatinga_filter['totalBens'] == df_ipatinga_filter[df_ipatinga_filter['DS_GENERO'] == 'FEMININO']['totalBens'].max())]
st.text('Maior bem declarado masculino')
df_ipatinga_filter[(df_ipatinga_filter['DS_GENERO'] == 'MASCULINO') & 
                   (df_ipatinga_filter['totalBens'] == df_ipatinga_filter[df_ipatinga_filter['DS_GENERO'] == 'MASCULINO']['totalBens'].max())]


