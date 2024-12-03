# Machine Learning-Driven Stock Market Decision Framework

Welcome to the repository for the research paper:  
**“Machine Learning-Driven Backtesting Framework for Stock Market Decision-Making: Integrating Technical Indicators and Predictive Models.”**  
This repository provides the code and resources to replicate our experiments and insights into stock market predictions across industries during the COVID-19 financial anomaly.

---

## Overview

This project investigates the effectiveness of machine learning models in predicting stock market movements in the **E-commerce (Amazon)** and **Finance (American Express)** industries. The focus is on the impact of the COVID-19 anomaly and the adaptability of models to such volatile conditions.

### Key Features:
- **Comparison of Models**: Benchmark model (Random Forest) vs. custom models (Voting Classifier combining XGBoost and Random Forest, and LightGBM).
- **Technical Indicators**: Leveraging RSI, ADX, NATR, and other derived features.
- **Backtesting Framework**: Evaluation through classification metrics and profitability analysis using simulated trading strategies.

---

## Repository Structure

```plaintext
.
├── Amazon Models (AMZN)/
│   ├── LGBM_amzn.ipynb                # Light GBM Amazon
│   ├── RFmodel_amzn.ipynb             # Random Forest Amazon
│   └── XG_RFmodel_amzn.ipynb          # Voting Classifier XGBoost and Random Forest Amazon
├── American Express Models (AXP)/           
│   ├── LGBM_axp.ipynb                 # Light GBM American Express
│   ├── RFmodel_axp.ipynb              # Random Forest American Express
│   └── XG_RFmodel_axp.ipynb           # Voting Classifier XGBoost and Random Forest American Express
├── datasets/
│   ├── amzn_data.csv                  # Amazon dataset
│   ├── data.py                        # code to clean and formats the data 
│   ├── historical_stock_data.csv      # Stock data from Yahoo Finance 
│   └── axp_data.csv                   # American Express dataset
├── README.md                          # Project overview (this file)  
├── Portfolio Simulation/
│    └──Portfolio.ipynb
└── requirements.txt                   # Dependencies and library requirements  
