import streamlit as st
import pandas as pd
import sqlite3

st.title('Local Food Wastage Management System')
conn = sqlite3.connect('food_waste_management.db')

menu = ['View Food Listings', 'Add Food Listing', 'Update Food Listing', 'Delete Food Listing',
        'View Claims', 'Add Claim', 'Update Claim', 'Delete Claim', 'Analysis']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'View Food Listings':
    df = pd.read_sql_query('SELECT * FROM food_listings', conn)
    city = st.selectbox('Filter by City', ['All'] + list(df['Location'].unique()))
    if city != 'All':
        df = df[df['Location'] == city]
    st.dataframe(df)

elif choice == 'Add Food Listing':
    st.subheader('Add New Food Listing')
    st.info('Form implementation here')

elif choice == 'Update Food Listing':
    st.subheader('Update Food Listing')
    st.info('Update form implementation here')

elif choice == 'Delete Food Listing':
    st.subheader('Delete Food Listing')
    st.info('Delete form implementation here')

elif choice == 'View Claims':
    df = pd.read_sql_query('SELECT * FROM claims', conn)
    st.dataframe(df)

elif choice == 'Add Claim':
    st.subheader('Add New Claim')
    st.info('Form implementation here')

elif choice == 'Update Claim':
    st.subheader('Update Claim')
    st.info('Update form implementation here')

elif choice == 'Delete Claim':
    st.subheader('Delete Claim')
    st.info('Delete form implementation here')

elif choice == 'Analysis':
    st.subheader('Data Analysis & Visualizations')
    provider_donated = pd.read_sql_query("""
        SELECT p.Name, SUM(f.Quantity) as Total_Donated
        FROM food_listings f
        JOIN providers p ON f.Provider_ID = p.Provider_ID
        GROUP BY p.Name
        ORDER BY Total_Donated DESC
        LIMIT 5
    """, conn)
    st.bar_chart(provider_donated.set_index('Name'))

conn.close()
