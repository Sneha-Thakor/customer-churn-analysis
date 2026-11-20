# Customer Churn Analysis

## Project Overview
Customer Churn Analysis is a data analytics project focused on identifying customer churn patterns and understanding the factors associated with customer attrition in the telecom industry.

The project uses Python for data analysis and visualization, and Streamlit to build an interactive dashboard.

## Objectives
- Analyze customer churn and retention rates.
- Identify customer segments with higher churn rates.
- Analyze churn based on contract type, internet service, payment method and tenure.
- Explore the relationship between monthly charges and churn.
- Provide business recommendations to improve customer retention.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

## Dataset
The project uses the Telco Customer Churn dataset containing customer information, service details, billing data and churn status.

## Key Metrics
- Total Customers: 7,043
- Churned Customers: 1,869
- Retained Customers: 5,174
- Churn Rate: 26.54%
- Retention Rate: 73.46%

## Key Findings
- Month-to-month customers have the highest churn rate.
- Customers with shorter tenure are more likely to churn.
- Electronic check users show comparatively higher churn.
- Fiber optic customers show relatively high churn.
- Customers without Online Security and Tech Support services show higher churn patterns.

## Dashboard Features
- Interactive customer filters
- Customer overview KPI metrics
- Customer churn distribution
- Churn rate by contract
- Churn rate by internet service
- Churn rate by payment method
- Churn analysis by tenure
- Monthly charges analysis
- Customer data table

## Project Structure
Customer Churn Analysis/
├── data/
│   └── Customer_Churn_Analysis.csv
├── visuals/
├── reports/
├── app.py
├── analysis.py
├── requirements.txt
└── README.md

## How to Run

### 1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_LINK

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the analysis
python analysis.py

### 4. Launch the dashboard
python -m streamlit run app.py

## Business Recommendations
- Encourage month-to-month customers to opt for longer-term contracts.
- Improve onboarding and support for new customers.
- Review pricing and service satisfaction among high-churn segments.
- Promote Online Security and Tech Support services.
- Develop targeted retention campaigns for customers at risk of leaving.

## Conclusion
This project demonstrates the use of data analysis, visualization and dashboard development to uncover customer churn patterns and support data-driven business decisions.

**Tools:** Python | Pandas | NumPy | Matplotlib | Seaborn | Streamlit
