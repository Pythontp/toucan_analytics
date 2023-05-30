import streamlit as st
import matplotlib.pyplot as plt
import requests
import json
import streamlit as st
from django.http import request
import streamlit as st
import pandas as pd
import altair as alt


import streamlit as st

# Define options for the dropdown
options = ['Table', 'Mode of Transanction', 'PIE Chart']


get_method=requests.get('http://127.0.0.1:8000/analytics/?type=table')
if get_method.status_code == 200:
    # Extract the data from the response
    data = get_method.json()
    customer = data['customer']
    mode = data['values']
    
# Create a sample data frame
    data = {
        'Customer Id': [i for i in customer],
        'Frequent mode of Transanction': [i for i in mode],
    }
    df = pd.DataFrame(data)
    # Add a serial number column
    df.insert(0, 'S.No', range(1, len(df) + 1))
    # Convert DataFrame to HTML table without index column
    html_table = df.to_html(index=False)
    # Display the table
    st.write(html_table, unsafe_allow_html=True)
else:
    st.error(f'Error: {get_method.status_code}')




