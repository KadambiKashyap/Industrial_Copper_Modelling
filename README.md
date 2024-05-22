# Copper Industry Sales and Lead Prediction

## Problem Statement
The copper industry deals with sales and pricing data that may suffer from skewness and noise, affecting manual prediction accuracy. Manual handling of these challenges is time-consuming and may not yield optimal pricing decisions. A machine learning regression model can address these issues using techniques such as data normalization, feature scaling, and outlier detection, and leveraging algorithms robust to skewed and noisy data.

Another challenge in the copper industry is capturing leads. A lead classification model evaluates and classifies leads based on their likelihood to become customers. By using the `STATUS` variable, where `WON` is considered a success and `LOST` is considered a failure, we can create a model to predict lead outcomes.

## Solution Approach
1. **Data Exploration:**
   - Explore skewness and outliers in the dataset.
   - Transform data into a suitable format and perform necessary cleaning and preprocessing.

2. **Regression Model:**
   - Predict the continuous variable `Selling_Price`.

3. **Classification Model:**
   - Predict the lead status (`WON` or `LOST`).

4. **Streamlit Page:**
   - Create a page where users can input column values to get predicted `Selling_Price` or lead `Status`.

## About the Data
- `id`: Unique identifier for each transaction or item.
- `item_date`: Date of the transaction or item occurrence.
- `quantity_tons`: Quantity of the item in tons.
- `customer`: Customer identifier.
- `country`: Country associated with each customer.
- `status`: Current status of the transaction or item (`Draft`, `Won`).
- `item_type`: Category of the items.
- `application`: Specific use or application of the items.
- `thickness`: Thickness of the items.
- `width`: Width of the items.
- `material_ref`: Reference or identifier for the material used.
- `product_ref`: Reference or identifier for the specific product.
- `delivery_date`: Expected or actual delivery date.
- `selling_price`: Price at which items are sold.


## Learning Outcomes
- Proficiency in Python and libraries like Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, and Streamlit.
- Experience in data preprocessing, outlier detection, and data normalization.
- Understanding and visualizing data using EDA techniques.
- Applying machine learning techniques for regression and classification.
- Building and optimizing machine learning models using evaluation metrics and techniques.
- Feature engineering to create informative data representations.
- Developing a web application using Streamlit.
- Understanding manufacturing domain challenges and solutions through machine learning.

## Acknowledgments
- KADAMBI V KASHYAP
