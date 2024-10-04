import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    data = pd.read_csv('D:/codeng/bangkit/submission/dashboard/main_data.csv')
    return data

data = load_data()

st.title('Analisis Rental Sepeda')
st.write("Data Rental Sepeda")
st.write(data.head())

st.subheader("Total dan Rata-rata Rental Sepeda per Musim")
season_group = data.groupby('season').agg({'cnt': ['sum', 'mean'], 'casual': 'mean', 'registered': 'mean'}).reset_index()

fig, ax = plt.subplots(2, 1, figsize=(8, 6))

ax[0].plot(season_group['season'], season_group[('casual', 'mean')], marker='o', color='blue', label='Casual')
ax[0].set_title('Rata-rata Casual Rental per Musim')
ax[0].legend()

ax[1].plot(season_group['season'], season_group[('registered', 'mean')], marker='o', color='green', label='Registered')
ax[1].set_title('Rata-rata Registered Rental per Musim')
ax[1].legend()

st.pyplot(fig)

st.subheader("Total dan Rata-rata Rental Sepeda per Bulan")
month_group = data.groupby('mnth').agg({'cnt': ['sum', 'mean'], 'casual': 'mean', 'registered': 'mean'}).reset_index()

fig, ax = plt.subplots(2, 1, figsize=(8, 6))

ax[0].plot(month_group['mnth'], month_group[('casual', 'mean')], marker='o', color='blue', label='Casual')
ax[0].set_title('Rata-rata Casual Rental per Bulan')
ax[0].legend()

ax[1].plot(month_group['mnth'], month_group[('registered', 'mean')], marker='o', color='green', label='Registered')
ax[1].set_title('Rata-rata Registered Rental per Bulan')
ax[1].legend()

st.pyplot(fig)

st.subheader("Perbandingan Rata-rata Casual dan Registered Rental dalam Holiday dan Workingday")
holiday_group = data.groupby('holiday').agg({'casual': 'mean', 'registered': 'mean'}).reset_index()

st.write(holiday_group)

fig, ax = plt.subplots()
ax.bar(holiday_group['holiday'] - 0.2, holiday_group['casual'], width=0.4, label='Casual')
ax.bar(holiday_group['holiday'] + 0.2, holiday_group['registered'], width=0.4, label='Registered')
ax.set_title('Rata-rata Casual dan Registered Rental (Holiday vs Workingday)')
ax.set_xlabel('Holiday (0 = Workingday, 1 = Holiday)')
ax.set_ylabel('Rata-rata Rental')
ax.legend()
st.pyplot(fig)

st.subheader("Perbandingan Rata-rata Casual dan Registered Rental dalam Weather")
weather_group = data.groupby('weathersit').agg({'casual': 'mean', 'registered': 'mean'}).reset_index()

st.write(weather_group)

fig, ax = plt.subplots()
ax.bar(weather_group['weathersit'] - 0.2, weather_group['casual'], width=0.4, label='Casual')
ax.bar(weather_group['weathersit'] + 0.2, weather_group['registered'], width=0.4, label='Registered')
ax.set_title('Rata-rata Casual dan Registered Rental per Kondisi Cuaca')
ax.set_xlabel('Kondisi Cuaca (1-4)')
ax.set_ylabel('Rata-rata Rental')
ax.legend()
st.pyplot(fig)
