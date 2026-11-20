
import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------- PAGE SETTINGS --------------------

st.set_page_config(
    page_title="Customer Churn Analytics",
    page_icon="📊",
    layout="wide"
)

# -------------------- DESIGN --------------------

st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}

[data-testid="stMetric"] {
    background-color: #1c2333;
    padding: 15px;
    border-radius: 10px;
}

h1, h2, h3 {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -------------------- LOAD DATA --------------------

@st.cache_data
def load_data():

    data = pd.read_csv("data/Customer_Churn_Analysis.csv")

    data["TotalCharges"] = pd.to_numeric(
        data["TotalCharges"], errors="coerce"
    )

    data["TotalCharges"] = data["TotalCharges"].fillna(0)

    return data


df = load_data()

# -------------------- TITLE --------------------

st.title("📊 Customer Churn Analytics")

st.markdown(
    "Explore customer behavior, churn patterns and retention performance."
)

# -------------------- SIDEBAR FILTERS --------------------

st.sidebar.header("Dashboard Filters")


contract_options = ["All"] + sorted(
    df["Contract"].dropna().unique().tolist()
)

selected_contract = st.sidebar.selectbox(
    "Contract",
    contract_options
)

internet_options = ["All"] + sorted(
    df["InternetService"].dropna().unique().tolist()
)

selected_internet = st.sidebar.selectbox(
    "Internet Service",
    internet_options
)

gender_options = ["All"] + sorted(
    df["gender"].dropna().unique().tolist()
)

selected_gender = st.sidebar.selectbox(
    "Gender",
    gender_options
)

# -------------------- APPLY FILTERS --------------------

filtered_df = df.copy()

if selected_contract != "All":

    filtered_df = filtered_df[
        filtered_df["Contract"] == selected_contract
    ]

if selected_internet != "All":

    filtered_df = filtered_df[
        filtered_df["InternetService"] == selected_internet
    ]

if selected_gender != "All":

    filtered_df = filtered_df[
        filtered_df["gender"] == selected_gender
    ]

# -------------------- CALCULATE KPIs --------------------

total_customers = len(filtered_df)

churned_customers = len(
    filtered_df[filtered_df["Churn"] == "Yes"]
)

retained_customers = len(
    filtered_df[filtered_df["Churn"] == "No"]
)

if total_customers > 0:

    churn_rate = (
        churned_customers / total_customers
    ) * 100

    retention_rate = (
        retained_customers / total_customers
    ) * 100

    average_charges = filtered_df["MonthlyCharges"].mean()

else:

    churn_rate = 0
    retention_rate = 0
    average_charges = 0

# -------------------- KPI CARDS --------------------

st.subheader("Customer Overview")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Customers", f"{total_customers:,}")

col2.metric("Churned Customers", f"{churned_customers:,}")

col3.metric("Churn Rate", f"{churn_rate:.2f}%")

col4.metric("Retention Rate", f"{retention_rate:.2f}%")

col5.metric("Avg. Monthly Charges", f"${average_charges:.2f}")

# -------------------- CHURN DISTRIBUTION --------------------

st.subheader("📊 Churn Distribution")

col1, col2 = st.columns([2, 1])

with col1:

    churn_data = filtered_df["Churn"].value_counts().reset_index()

    churn_data.columns = ["Churn", "Customers"]

    fig = px.pie(
        churn_data,
        names="Churn",
        values="Customers",
        hole=0.55,
        color="Churn",
        color_discrete_map={
            "Yes": "#FF4B6E",
            "No": "#22C55E"
        }
    )

    fig.update_traces(
        textinfo="label+percent",
        textposition="inside"
    )

    fig.update_layout(
        template="plotly_dark",
        legend=dict(
            orientation="h",
            y=-0.15
        )
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    st.markdown("### Customer Summary")

    st.metric("Retained Customers", f"{retained_customers:,}")

    st.metric("Churned Customers", f"{churned_customers:,}")

    st.metric("Overall Churn", f"{churn_rate:.2f}%")

    st.metric("Overall Retention", f"{retention_rate:.2f}%")

# -------------------- CHURN BY CONTRACT --------------------

st.subheader("📄 Churn by Contract Type")

contract_data = filtered_df.groupby(
    ["Contract", "Churn"]
).size().reset_index(name="Customers")

fig = px.bar(
    contract_data,
    x="Contract",
    y="Customers",
    color="Churn",
    barmode="group",
    color_discrete_map={
        "Yes": "#F59E0B",
        "No": "#60A5FA"
    },
    template="plotly_dark"
)

fig.update_layout(
    xaxis_title="Contract",
    yaxis_title="Customers"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------- CHURN BY INTERNET SERVICE --------------------

st.subheader("🌐 Churn by Internet Service")


internet_data = filtered_df.groupby(
    ["InternetService", "Churn"]
).size().reset_index(name="Customers")

fig = px.bar(
    internet_data,
    x="Customers",
    y="InternetService",
    color="Churn",
    barmode="group",
    orientation="h",
    color_discrete_map={
        "Yes": "#A78BFA",
        "No": "#34D399"
    },
    template="plotly_dark"
)

fig.update_layout(
    xaxis_title="Customers",
    yaxis_title="Internet Service"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------- CHURN BY PAYMENT METHOD --------------------

st.subheader("💳 Churn by Payment Method")

payment_data = filtered_df.groupby(
    ["PaymentMethod", "Churn"]
).size().reset_index(name="Customers")

fig = px.bar(
    payment_data,
    x="Customers",
    y="PaymentMethod",
    color="Churn",
    barmode="group",
    orientation="h",
    color_discrete_map={
        "Yes": "#F472B6",
        "No": "#38BDF8"
    },
    template="plotly_dark"
)

fig.update_layout(
    xaxis_title="Customers",
    yaxis_title="Payment Method"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------- CHURN BY TENURE --------------------

st.subheader("📅 Churn by Customer Tenure")

filtered_df = filtered_df.copy()

filtered_df["TenureGroup"] = pd.cut(
    filtered_df["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=[
        "0-12 Months",
        "13-24 Months",
        "25-48 Months",
        "49-72 Months"
    ]
)

tenure_data = filtered_df.groupby(
    ["TenureGroup", "Churn"],
    observed=False
).size().reset_index(name="Customers")

fig = px.bar(
    tenure_data,
    x="TenureGroup",
    y="Customers",
    color="Churn",
    barmode="group",
    color_discrete_map={
        "Yes": "#FB7185",
        "No": "#FBBF24"
    },
    template="plotly_dark"
)

fig.update_layout(
    xaxis_title="Customer Tenure",
    yaxis_title="Customers"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------- MONTHLY CHARGES --------------------

st.subheader("💰 Monthly Charges: Churned vs Retained")

fig = px.histogram(
    filtered_df,
    x="MonthlyCharges",
    color="Churn",
    nbins=30,
    barmode="overlay",
    opacity=0.7,
    color_discrete_map={
        "Yes": "#EF4444",
        "No": "#6366F1"
    },
    template="plotly_dark"
)

fig.update_layout(
    xaxis_title="Monthly Charges",
    yaxis_title="Number of Customers"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------- CHURN BY ONLINE SECURITY --------------------

st.subheader("🔐 Churn by Online Security")

security_data = filtered_df.groupby(
    ["OnlineSecurity", "Churn"]
).size().reset_index(name="Customers")

fig = px.bar(
    security_data,
    x="OnlineSecurity",
    y="Customers",
    color="Churn",
    barmode="group",
    color_discrete_map={
        "Yes": "#818CF8",
        "No": "#2DD4BF"
    },
    template="plotly_dark"
)

fig.update_layout(
    xaxis_title="Online Security",
    yaxis_title="Customers"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------- CHURN BY TECH SUPPORT --------------------

st.subheader("🛠️ Churn by Tech Support")

support_data = filtered_df.groupby(
    ["TechSupport", "Churn"]
).size().reset_index(name="Customers")

fig = px.bar(
    support_data,
    x="TechSupport",
    y="Customers",
    color="Churn",
    barmode="group",
    color_discrete_map={
        "Yes": "#C084FC",
        "No": "#FDBA74"
    },
    template="plotly_dark"
)

fig.update_layout(
    xaxis_title="Tech Support",
    yaxis_title="Customers"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------- CUSTOMER DATA EXPLORER --------------------

st.subheader("🔍 Customer Data Explorer")

st.write(
    "Explore customer records using the selected dashboard filters."
)

st.dataframe(
    filtered_df,
    use_container_width=True
)

# -------------------- DOWNLOAD DATA --------------------

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Customer Data",
    data=csv_data,
    file_name="customer_churn_filtered_data.csv",
    mime="text/csv"
)

# -------------------- FOOTER --------------------

st.markdown("---")

st.caption(
    "Customer Churn Analytics | Python | Pandas | Streamlit | Plotly"
)
