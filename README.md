# Crop Price Prediction 
This project analyzes wholesale food prices in Kenya, specifically for various crops across different markets and counties. The goal is to gain insights into the trends and patterns of food prices over time and across different regions.

## Table of Contents

- [Features](#features)
- [Usage](#Usage)
- [Installation](#installation)
- [Data Description](#Data-Description)
- [Data Preprocessing](#Data-Preprocessing)
- [Analysis and Visualization](#Analysis-and-Visualization)
- [Contributing](#contributing)
- [Authors](#Authors)

## Features
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Feature engineering
- Outlier detection and removal
- Data visualization
- Potential machine learning model building (if applicable)

## Usage
1. Clone the repository.

          git clone git@github.com:pseudocmd/Phase5-project.git
3. Install the required dependencies.
4. Run the Jupyter Notebook or Python script to execute the code.
5. Follow the instructions and comments in the code for specific tasks or analyses.

## Installation
To run the code in this project, you'll need:
- Python 3
- numpy
- matplotlib
- seaborn
- scikit-learn

You can install the dependencies using pip:

      pip install pandas numpy matplotlib seaborn scikit-learn


## Data Description
The dataset contains the following columns:

- Product: Type of food product.
- Market Location: Location of the market where the product is sold.
- Wholesale Price: Wholesale price of the product.
- Supply Volume: Volume of supply for the product.
- County: County where the market is located.
- Date: Date of the record.
- USD Rate: USD exchange rate.
- Additional engineered features: Ratio of supply volume to wholesale price, one-hot encoded product and market location, date-time features, lag features, rolling window statistics, and differenced features.


## Data Preprocessing
The preprocessing steps include:

- Cleaning the data by removing outliers and irrelevant entries
- Feature engineering to create new features like supply volume ratio and one-hot encoding
- Handling missing values and converting data types
- Extracting date-time features and creating lag features
- Normalizing numerical features

## Analysis and Visualization
The analysis and visualization techniques employed in this project include:

- Boxplots to visualize price distributions by product and county
- Scatter plots to explore relationships between price, supply volume, and USD rate
- Line charts to visualize trends over time for price and USD rate
- Statistical analysis to identify correlations and trends

## Contributing
We welcome contributions from the community. If you'd like to contribute to this project, please follow these steps:

### Fork the repository.
1. Create a new branch for your feature:

        git checkout -b feature-name.
   
2. Make your changes and commit them:
 
       git commit -m 'Add feature-name'.
3. Push to the branch:
  
       git push origin feature-name.
   
4. Create a pull request.

## Authors
- Milton Kabute
- Collins Cheruiyot
- Thorne Makau
- Joyce Muthiani
- Kenneth Karanja
- Amina Hagi
