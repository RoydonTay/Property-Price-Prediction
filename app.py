import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

# Introductory text
st.markdown("# SG Condominium Price Prediction")
# Link to my repo
'''
    Created by: Roydon Tay [![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/RoydonTay)    
'''
st.markdown("<br>",unsafe_allow_html=True)
st.markdown(
'''
In my personal project I have trained a random forest regressor model to produce price predictions 
for condominiums with a lease period within 100 years. It is trained on private property 
transaction data from 2017-2022, provided by URA's API.
## Using the web app:
Fill up your input and hit the 'Submit' button to see prediction output and visualisation plots.
''')
st.markdown(
'''
Don't have a property in mind yet? Try the model with the current values to see what a unit in 
RIVERPARC RESIDENCE (Punggol Drive) might cost!
'''
)

# Takes user inputs. Starts with defualt values for user to see sample prediction output.
area = st.text_input(
    "Floor Area (sq m):",
    value=125
)

lease_left = st.slider('Lease Left', 0, 100, value=86)

st.markdown('''
SVY21 Coordinates:
\nTo get the coordinates value, use the Google Maps 'pointer' function to get Latitude 
and Longtitude values, and use the coordinates converter on this 
[website](https://dominoc925-pages.appspot.com/webapp/calc_svy21/default.html).
\nx-coordinate = easting, y-coordinate = northing
'''
)

x = st.text_input(
    "x-coordinate:",
    value=37324.10899,
)

y = st.text_input(
    "y-coordinate:",
    value=42209.54801,
)

floor_range = st.selectbox(
    "Please select floor range of property:",
    ("01-05", "06-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40",
    "41-45", "46-50", "51-55", "56-60", "61-65", "66-70", "71-75", "B1-B5"),
)

property_type = st.selectbox(
    "Please select floor range of property (Strata types only):",
    ("Executive Condominium", "Apartment", "Condominium"),
)

# Downloading and unzipping model pickle file in GitHub Repo
# Caching used so that model is loaded only once when app is first launched
@st.cache_data
def load_model():
    loaded_model = pickle.load(open('best_model.pkl', 'rb'))
    return loaded_model

@st.cache_data
def load_data():
    return pd.read_pickle(r"Data\final_features.pkl")

model = load_model()

# Button to run model. Normalisation processing on inputs input data and generation of prediction and viz plots.
if st.button('Submit'):
    # Convert numerical inputs to float
    area_float = (float(area) - 32) / (1961 - 32)
    x_float = (float(x) - 12779.295898) / (43274.605469 - 12779.295898)
    y_float = (float(y) - 24730.345703) / (48642.828125 - 24730.345703)
    lease_left_float = (float(lease_left) - 16)/ (99 - 16)

    # Convert categorical inputs into numerical labels
    floor_lst = ["01-05", "06-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40", "41-45", 
                 "46-50", "51-55", "56-60", "61-65", "66-70", "71-75", "B1-B5"]
    floor_encoded = floor_lst.index(floor_range) / 14
    prop_lst = ["Executive Condominium", "Apartment", "Condominium"]
    prop_encoded = prop_lst.index(property_type) / 5

    # Generate prediction
    data_input = np.array([area_float, floor_encoded, prop_encoded, lease_left_float, x_float, y_float])
    data_input = data_input.reshape(1, -1)
    prediction = model.predict(data_input)
    st.markdown("Estimated Price of Property: **${}**".format(round(prediction.item(0), 2)))
    
    loaded_data = load_data()

    # Area plot
    area_plot = sns.displot(data=loaded_data, x="num_area", kind='kde')
    # adding a vertical line for input data
    area_plot.refline(x= area_float, ls='--', lw=2)

    # Lease left plot
    lease_plot = sns.displot(data=loaded_data, x="lease_left", kind='kde')
    # adding a vertical line for input data
    lease_plot.refline(x= lease_left_float, ls='--', lw=2)

    with st.container():
        st.markdown("### Property floor area compared to others in dataset:")
        st.markdown("Dotted line represents floor area of your input")
        st.pyplot(area_plot.figure)
        st.markdown("### Property lease left compared to others in dataset:")
        st.markdown("Dotted line represents lease left of your input")
        st.pyplot(lease_plot.figure)

else:
    st.write('Click button to see price prediction')

st.markdown(
'''
## Disclaimer:
- Whilst every effort has been taken during the development of this model for it to be as accurate and reliable as possible it 
is important that the user understands its outputs are still predictions and not absolute. Any decisions taken whist using this 
tool are the responsibility of the user and no liability whatsoever will be taken by me.
- This project was intended to be used for my portfolio and not for individual use.
- Finally, the model is trained with past data and may become outdated with time as the property market changes. I may no longer 
create any updated versions. This model was trained with data retrieved on: 17/06/2022

### Model Accuracy on Test Split Data (For reference):
- Mean Absolute Error: 49871.847780550044"
- Root Mean Squared Error: 129728.00314684339
'''
)