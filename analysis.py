
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# -------------------- LOAD DATA --------------------

df = pd.read_csv("data/Customer_Churn_Analysis.csv")

print("\nDataset loaded successfully!")
print("Original dataset shape:", df.shape)


# -------------------- CLEAN DATA --------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Remove customer ID because it is not useful for analysis
if "customerID" in df.columns:
    df = df.drop("customerID", axis=1)

# Convert TotalCharges into numeric values
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

# Replace missing TotalCharges values with 0
df["TotalCharges"] = df["TotalCharges"].fillna(0)


print("\nData cleaning completed!")
print("Cleaned dataset shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())


# -------------------- BASIC INFORMATION --------------------

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())


# -------------------- CALCULATE KPIs --------------------

total_customers = len(df)

churned_customers = len(df[df["Churn"] == "Yes"])

retained_customers = len(df[df["Churn"] == "No"])


churn_rate = (churned_customers / total_customers) * 100

retention_rate = (retained_customers / total_customers) * 100


print("\nCUSTOMER KPIs")

print("Total Customers:", total_customers)

print("Churned Customers:", churned_customers)

print("Retained Customers:", retained_customers)

print("Churn Rate:", round(churn_rate, 2), "%")

print("Retention Rate:", round(retention_rate, 2), "%")


# -------------------- CREATE VISUALS FOLDER --------------------

os.makedirs("visuals", exist_ok=True)


# Use a consistent chart style
sns.set_style("whitegrid")


# -------------------- 1. CHURN DISTRIBUTION --------------------

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Churn",
    hue="Churn",
    palette={"No": "seagreen", "Yes": "tomato"},
    legend=False
)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("visuals/01_churn_distribution.png")

plt.close()


# -------------------- 2. CHURN BY CONTRACT --------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Contract",
    hue="Churn",
    palette={"No": "seagreen", "Yes": "tomato"}
)

plt.title("Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("visuals/02_churn_by_contract.png")

plt.close()


# -------------------- 3. CHURN BY INTERNET SERVICE --------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="InternetService",
    hue="Churn",
    palette={"No": "seagreen", "Yes": "tomato"}
)

plt.title("Churn by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("visuals/03_churn_by_internet.png")

plt.close()


# -------------------- 4. CHURN BY PAYMENT METHOD --------------------

plt.figure(figsize=(10, 5))

sns.countplot(
    data=df,
    x="PaymentMethod",
    hue="Churn",
    palette={"No": "seagreen", "Yes": "tomato"}
)

plt.title("Churn by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig("visuals/04_churn_by_payment.png")

plt.close()


# -------------------- 5. CHURN BY TENURE GROUP --------------------

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=[
        "0-12 Months",
        "13-24 Months",
        "25-48 Months",
        "49-72 Months"
    ]
)


plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="TenureGroup",
    hue="Churn",
    palette={"No": "seagreen", "Yes": "tomato"}
)

plt.title("Churn by Customer Tenure")
plt.xlabel("Tenure Group")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("visuals/05_churn_by_tenure.png")

plt.close()


# -------------------- 6. MONTHLY CHARGES --------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="MonthlyCharges",
    hue="Churn",
    bins=30,
    multiple="layer",
    palette={"No": "seagreen", "Yes": "tomato"}
)

plt.title("Monthly Charges: Churned vs Retained")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("visuals/06_monthly_charges.png")

plt.close()


# -------------------- 7. CHURN BY GENDER --------------------

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="gender",
    hue="Churn",
    palette={"No": "seagreen", "Yes": "tomato"}
)

plt.title("Churn by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("visuals/07_churn_by_gender.png")

plt.close()


# -------------------- 8. CHURN BY SENIOR CITIZEN --------------------

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="SeniorCitizen",
    hue="Churn",
    palette={"No": "seagreen", "Yes": "tomato"}
)

plt.title("Churn by Senior Citizen")
plt.xlabel("Senior Citizen (0 = No, 1 = Yes)")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("visuals/08_churn_by_senior.png")

plt.close()


# -------------------- 9. ONLINE SECURITY AND TECH SUPPORT --------------------

plt.figure(figsize=(10, 5))

sns.countplot(
    data=df,
    x="OnlineSecurity",
    hue="Churn",
    palette={"No": "seagreen", "Yes": "tomato"}
)

plt.title("Churn by Online Security")
plt.xlabel("Online Security")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("visuals/09_churn_by_security.png")

plt.close()


plt.figure(figsize=(10, 5))

sns.countplot(
    data=df,
    x="TechSupport",
    hue="Churn",
    palette={"No": "seagreen", "Yes": "tomato"}
)

plt.title("Churn by Tech Support")
plt.xlabel("Tech Support")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig("visuals/10_churn_by_support.png")

plt.close()


# -------------------- CHURN RATE BY CONTRACT --------------------

contract_churn = df.groupby("Contract")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\n========== CHURN RATE BY CONTRACT ==========")

print(contract_churn.round(2))


# -------------------- CHURN RATE BY INTERNET SERVICE --------------------

internet_churn = df.groupby("InternetService")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\nCHURN RATE BY INTERNET SERVICE")

print(internet_churn.round(2))


# -------------------- CHURN RATE BY TENURE GROUP --------------------

tenure_churn = df.groupby(
    "TenureGroup", observed=False
)["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\nCHURN RATE BY TENURE")

print(tenure_churn.round(2))


# -------------------- FINAL INSIGHTS --------------------

print("\nBUSINESS INSIGHTS")


# Contract insight
highest_contract_churn = contract_churn.idxmax()

print(
    "Highest churn among contract types:",
    highest_contract_churn
)


# Internet service insight
highest_internet_churn = internet_churn.idxmax()

print(
    "Highest churn among internet services:",
    highest_internet_churn
)


# Tenure insight
highest_tenure_churn = tenure_churn.idxmax()

print(
    "Highest churn among tenure groups:",
    highest_tenure_churn
)

print("\nAnalysis completed successfully!")
