# SG-Property-Price-Prediction
## About Project
In this personal project, I attempt the different stages of an end-to-end data science project. This project uses a dataset from the [Urban Redevelopment Authority (URA) API](https://www.ura.gov.sg/maps/api/#private-residential-property). It contains over 100,000 private property transactions between 2017-2022 in Singapore.

## Summary of Project 

### Outline:
1. Acquiring Dataset from REST API (see [API_data_extraction.py](https://github.com/RoydonTay/Property-Price-Prediction/blob/main/API_data_extraction.py))
2. Data Processing, Feature Extraction & Exploratory Data Analysis (see [Exploratory_Data_Analysis.ipynb](https://github.com/RoydonTay/Property-Price-Prediction/blob/main/Exploratory_Data_Analysis.ipynb))
3. Model Training, Experimentation and Selection (see [Model_selection_experimentation.ipynb](https://github.com/RoydonTay/Property-Price-Prediction/blob/main/Model_selection_experimentation.ipynb))
4. Hosted a simple app on Streamlit that allows users to try generating predictions for different inputs using the model. [Click to see app.](https://sg-property-price-prediction.streamlit.app)

### Key Findings:
- After pivoting the project to only focus on Condominiums with lease within 100 years, prediction accuracy improved significantly (MAE reduced by 82.4%). Focusing only on landed properties did not achieve any improvement. This could mean the prices of landed property rely more heavily on other features not considered in this dataset.
- **Best performing model type**: After testing Tree-based (Random Forest and XGBoost), Linear (Ridge Regression) and Neural Network (Multi-layer Perceptron), Random Forest model performed the best. 
- **Limitations**: Some properties are highly unlikely to be transacted (E.g. Units that are too old), and will not be represented in the dataset. The final model trained did not perform well in predicting properties that are not well represented by data points (properties with lease left < 40 years). Due to this limitation, the model cannot perform reliably in extrapolating the value of property over time.

### Possible future iterations:
- Merging of dataset with data from OneMap API, to get additional features such as proximity of property to facilities and amenities.

### Personal reflections:
- Completing this project allowed me to get my hands dirty with multiple python data science packages. Finding a dataset myself instead of picking one from Kaggle allowed me to learn methods of obtaining data (tried webscraping and APIs), and methods of cleaning and processing the data myself. 
- While the decisions I made during the data processing and model training and selection may not be the best, they allowed me to practice searching the web and learning from other projects and articles to decide the next step I should try.
