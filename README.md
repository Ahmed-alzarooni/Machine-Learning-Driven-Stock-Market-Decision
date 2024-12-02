Machine Learning-Driven Stock Market Decision Framework

Welcome to the repository for the research paper: “Machine Learning-Driven Backtesting Framework for Stock Market Decision-Making: Integrating Technical Indicators and Predictive Models.” This repository provides the code and resources to replicate our experiments and insights into stock market predictions across industries during the COVID-19 financial anomaly.

Overview

This project investigates the effectiveness of machine learning models in predicting stock market movements in the E-commerce (Amazon) and Finance (American Express) industries. The focus is on the impact of the COVID-19 anomaly and the adaptability of models to such volatile conditions.

Key features:
	•	Comparison of Models: Benchmark model (Random Forest) vs. custom models (Voting Classifier combining XGBoost and Random Forest, and LightGBM).
	•	Technical Indicators: Leveraging RSI, ADX, NATR, and other derived features.
	•	Backtesting Framework: Evaluation through classification metrics and profitability analysis using simulated trading strategies.

Repository Structure

.
├── Amazon Models (AMZN)/
│   ├── LGBM_amzn.ipynb                # Light GBM Amazon
│   ├── RFmodel_amzn.ipynb             # Random Forest Amazon
│   └── XG_RFmodel_amzn.ipynb          # Voting classifier XGBoost and Random Forest Amazon
├── American Express Models (AXP)/           
│   ├── LGBM_axp.ipynb                 # Light GBM American Express
│   ├── RFmodel_axp.ipynb              # Random Forest American Express
│   └── XG_RFmodel_axp.ipynb           # Voting classifier XGBoost and Random Forest American Express
├── datasets/
│   ├── amzn_data.csv                  # Amazon dataset
│   └── axp_data.csv                   # American Express dataset
├── README.md                          # Project overview (this file)  
└── requirements.txt                   # Dependencies and library requirements  

Features and Models

Implemented Models

	1.	Random Forest (Benchmark): Used as a reference from the parent paper.
	2.	Voting Classifier: Combines XGBoost and Random Forest for enhanced performance.
	3.	LightGBM (LGBM): Optimized for speed and handling large datasets.

Technical Indicators

	•	Relative Strength Index (RSI)
	•	Average Directional Index (ADX)
	•	Normalized Average True Range (NATR)
	•	Correlation with moving averages
	•	Price differentials (Open-Close, Close-High, Close-Low)

How to Use

	1.	Clone the Repository

git clone https://github.com/Ahmed-alzarooni/Machine-Learning-Driven-Stock-Market-Decision.git  
cd Machine-Learning-Driven-Stock-Market-Decision  


	2.	Install Dependencies
Install the required Python libraries:

pip install -r requirements.txt  



Results and Insights

The findings highlight significant differences in model adaptability across industries:
	•	E-commerce (Amazon): Demonstrated resilience during the COVID-19 anomaly.
	•	Finance (American Express): Experienced notable volatility, testing the robustness of predictive models.

Advanced models like Voting Classifier and LightGBM consistently outperformed the Random Forest benchmark in accuracy, precision, and profitability metrics.

Future Work

	•	Expanding to other industries or sectors.
	•	Evaluating hybrid models for enhanced performance.
	•	Incorporating additional market anomalies for robustness testing.

Contributors

	•	Ahmed Alzarooni - Lead Contributor
	•	Abdulla Alnuaimi - Lead Contributor
