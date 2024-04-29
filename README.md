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

## INTRODUCTION
At Datawise Solutions, we specialize in offering cutting-edge data analytics and consulting services to help organizations of all sizes use the value of their data. With a team of professional data scientists, analysts, and consultants, we are committed to assisting organizations in gaining important insights, making educated decisions, and driving growth.


Our objective is straightforward: turn raw data into actionable intelligence. Whether you want to streamline operations, improve marketing tactics, improve customer experiences, or drive innovation, we have the knowledge and technology to help you convert data difficulties into opportunities.

From data collecting and cleansing to advanced analytics and predictive modeling, we provide a full portfolio of services that are tailored to your individual requirements. Our collaborative approach guarantees that we understand your specific business objectives and create solutions that produce demonstrable outcomes.

Datawise Solutions believes that the power of data is infinite. Let us be your reliable partner on the path to data-driven success.

Explore the possibilities with Datawise Solutions today!
## BUSINESS UNDERSTANDING 
According to a Business Daily article, Kenyan farmers earn less even while consumers pay more for food products since there is a significant price difference between farmers' and consumer pricing. Kenyan farmers' commodity prices are influenced by an inefficient market structure and intermediaries between producers and buyers. It is highlighted that middlemen determine market dynamics, resulting in divergent wholesale and retail prices in Kenyan markets. However, external variables such as subsidy schemes and currency fluctuations have influenced farmers' commodity prices, yet farmers continue to earn less than the market price established in Kenyan stores and markets.

According to the KARI research, agricultural productivity is declining due to limited market access.

## Stakeholders

1.Kenya Farmers Association

2.Small-scale Farmers

3.Government Agencies (e.g., Ministry of Agriculture, Central Bank of Kenya)

4.Agricultural Traders and Middlemen

5.Financial Institutions

6.Consumers
## PROBLEM STATEMENT
Farmers in Kenya frequently face huge differences between the prices they receive for their commodities and the amounts consumers pay in marketplaces. This disparity is mostly caused by inefficient market systems and the presence of intermediaries that profit from pricing inconsistencies. As a result, farmers struggle to obtain reasonable rates for their produce, despite the fact that agriculture is an important component of the country's GDP and a source of income for many people. To address this issue, a complete price forecasting system that uses historical and real-time data, as well as machine learning models, is urgently needed. Such a technology would provide farmers with forecast pricing updates, improve market transparency, and allow all players in the agricultural value chain to make informed decisions.
## OBJECTIVES 
Creating machine learning models to forecast crop output pricing using variables such as location, time, supply dynamics, and currency fluctuations.
Developing a user-friendly interface for farmers to receive predicted pricing updates and market segmentation data.


Using historical agricultural commodity prices and CBK currency data to create accurate forecasting models.

Farmers will receive training and support in order to efficiently use the price forecasting system.
## Data Description
The dataset contains the following columns:
- Date: The date of the exchange rate data.
- Price: The closing price of USD to KES exchange rate on that date.
- Open: The opening price of USD to KES exchange rate on that date.
- Low: The lowest price of USD to KES exchange rate on that date.
- Volume: Volume of USD to KES exchange transactions (seems to be mostly NaN values).
- Change %: Percentage change in the USD to KES exchange rate from the previous day.
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
