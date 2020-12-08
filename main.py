import streamlit as st
import pandas as pd
import numpy as np

st.title('Missouri Respiratory Illness Statistics')

DEATH_DATA = './MORespiratoryDeaths.csv'
MO_FLU_DATA = './MOFluData.csv'
YEAR = 'year'
WEEK = 'week'
DEATHS = 'deaths'
DISEASE = 'disease'
INFLUENZA_A = 'influenza a'
INFLUENZA_B = 'influenza b'
UNKNOWN_INFLUENZA = 'unknown influenza'
WEEKLY_TOTAL = 'weekly total'
FLU_YEAR = 'flu year'
FLU_WEEK = 'flu week'


@st.cache
def load_data(nrows, datasource):
    data = pd.read_csv(datasource, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data


# Load 10,000 rows of data into the dataframe.
death_data = load_data(10000, DEATH_DATA)
st.subheader('Deaths per week *')
death_year_filter = st.slider(YEAR, 2015, 2020)
filtered_death_data = death_data[death_data[YEAR] == death_year_filter]
st.bar_chart(data=filtered_death_data.set_index(WEEK)[[DEATHS]])

st.text('* Data for 2020 is incomplete')

mo_flu_data = load_data(500, MO_FLU_DATA)
st.subheader('MO Flu Infections')
mo_flu_year_filter = st.slider(FLU_YEAR, 2019, 2020)
filtered_mo_flu_data = mo_flu_data[mo_flu_data[FLU_YEAR] == mo_flu_year_filter]
st.bar_chart(data=filtered_mo_flu_data.set_index(FLU_WEEK)[[INFLUENZA_A, INFLUENZA_B, UNKNOWN_INFLUENZA]])

st.markdown('[Check Out My Github](https://github.com/greenfructose)')