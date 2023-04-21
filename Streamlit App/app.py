import streamlit as st
import numpy as np
import pickle
from zipfile import ZipFile

# loading the temp.zip and creating a zip object
with ZipFile("best_model.zip", 'r') as zObject:
    zObject.extract("best_model.pkl")
zObject.close()

# App interface
st.header("SG Private Property Price Prediction Web App" )
st.markdown("In my personal project I have trained a model to produce price predictions for strata properties, with a lease period within 100 years. It is trained on private property transaction data from 2017-2022, provided by URA's API. Code and developing process is shared in my [GitHub Repository](https://github.com/RoydonTay/Property-Price-Prediction).")
st.write("Don't have a property in mind yet? Click submit with the current values to see what a unit in RIVERPARC RESIDENCE (Punggol Drive) might cost!")


area = st.text_input(
    "Floor Area (sq m):",
    value=125
)

lease_left = st.slider('Lease Left', 0, 100, value=86)

st.write("SVY21 Coordinates:")
st.markdown("To get the coordinates value, use the Google Maps 'pointer' function to get Latitude and Longtitude values, and use the coordinates converter on this [website](https://dominoc925-pages.appspot.com/webapp/calc_svy21/default.html).")
st.write("x-coordinate = easting, y-coordinate = northing")

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
    ("Executive Condominium", "Apartment", "Condominium", "Strata Terrace", "Strata Semi-detached", "Strata Detached"),
)

# Button to run model
if st.button('Submit'):
    # Convert numerical inputs to float
    area_float = float(area)
    x_float = float(x)
    y_float = float(y)
    lease_left_float = float(lease_left)

    # Convert categorical inputs into numerical labels
    floor_lst = ["01-05", "06-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40", "41-45", "46-50", "51-55", "56-60", "61-65", "66-70", "71-75", "B1-B5"]
    floor_encoded = floor_lst.index(floor_range)
    prop_lst = ["Executive Condominium", "Apartment", "Condominium", "Strata Terrace", "Strata Semi-detached", "Strata Detached"]
    prop_encoded = prop_lst.index(property_type)

    # Load model and predict
    loaded_model = pickle.load(open("best_model.pkl", 'rb'))
    data_input = np.array([area_float, floor_encoded, prop_encoded, lease_left_float, x_float, y_float])
    data_input = data_input.reshape(1, -1)
    prediction = loaded_model.predict(data_input)
    st.write("Estimated Price of Property: ${}".format(round(prediction.item(0), 2)))

else:
    st.write('Click button to see price prediction')

st.markdown("**DISCLAIMER**:")
st.markdown("- Whilst every effort has been taken during the development of this model for it to be as accurate and reliable as possible it is important that the user understands its outputs are still predictions and not absolute. Any decisions taken whist using this tool are the responsibility of the user and no liability whatsoever will be taken by me.")
st.markdown("- This project was intended to be used for my portfolio and not for individual use.")
st.markdown("- Finally, the model is trained with past data and may become more outdated with time as the property market changes. I may no longer create any updated versions.")
st.markdown("Created by: Roydon Tay")
