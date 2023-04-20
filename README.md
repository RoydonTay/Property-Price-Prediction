# Property-Price-Prediction
## About Project
In this personal project, I attempt the different stages of an end-to-end data science project. This project uses a dataset from the Urban Redevelopment Authority (URA) API. It contains more than 100,000 private property transactions between 2017-2022.

## Summary of Project 
### Outline:
1. Acquiring Dataset from REST API (see [API_data_extraction.py](https://github.com/RoydonTay/Property-Price-Prediction/blob/main/API_data_extraction.py))
2. Data Processing, Feature Extraction & Exploratory Data Analysis (see [Exploratory_Data_Analysis.ipynb](https://github.com/RoydonTay/Property-Price-Prediction/blob/main/Exploratory_Data_Analysis.ipynb))
3. Model Training, Experimentation and Selection (see [Model_selection_experimentation.ipynb](https://github.com/RoydonTay/Property-Price-Prediction/blob/main/Model_selection_experimentation.ipynb))

### Key Findings
- With the current dataset, there may be insufficient data points and features for the model to generalize well and make accurate predicitions for landed and freehold porperties.
- After pivoting the project to only focus on Strata properties, prediction accuracy improved significantly.
- Best performing model type: After testing Tree-based (Random Forest), Linear (Ridge Regression) and Neural Network (Multi-layer Perceptron) models, Random Forest model performed the best. 

### Possible improvements for future iterations
- Merging of dataset with data from OneMap API, to get additional features such as proximity of property to facilities and amenities.
- Use of other types of models (that perform better on less representative datasets) to predict prices of landed properties.
- Possibly uploading the notebooks to Kaggle to get feedback from fellow Kagglers to improve my current process.

## Reflections
- Completing this project allowed me to get my hands dirty with multiple python data science packages. Finding a dataset myself instead of picking one from Kaggle allowed me to learn methods of obtaining data (tried webscraping and APIs), and methods of cleaning and processing the data myself. 
- While the decisions I made during the data processing and model training and selection may not be the best, they allowed me to practice searching the web and learning from other projects and articles to decide the next step I should try.
