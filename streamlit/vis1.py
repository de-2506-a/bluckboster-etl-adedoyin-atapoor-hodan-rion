import pandas as pd
import streamlit as st
import plotly.express as px


country_df = pd.read_csv("../data/processed/cleaned-country.csv")
city_df = pd.read_csv("../data/processed/cleaned-city.csv")
customer_df = pd.read_csv("../data/processed/cleaned-customers.csv")
rental_df = pd.read_csv("../data/processed/cleaned-rental.csv")
inventory_df = pd.read_csv("../data/processed/cleaned-inventory.csv")
film_df = pd.read_csv("../data/processed/cleaned-films.csv")
address_df = pd.read_csv("../data/processed/cleaned-address.csv")
payment_df = pd.read_csv("../data/processed/cleaned-payments.csv")

# Step 1: Merge country and city
merged_df = pd.merge(country_df, city_df.drop(columns=["last_update"], errors="ignore"), on="country_id", how="inner")

# Step 2: Merge sequentially with other DataFrames
merged_df = pd.merge(merged_df, address_df.drop(columns=["last_update"], errors="ignore"), on="city_id", how="inner")
merged_df = pd.merge(merged_df, customer_df.drop(columns=["last_update"], errors="ignore"), on="address_id", how="inner")
merged_df = pd.merge(merged_df, rental_df.drop(columns=["last_update"], errors="ignore"), on="customer_id", how="inner")
merged_df = pd.merge(merged_df, inventory_df.drop(columns=["last_update"], errors="ignore"), on="inventory_id", how="inner")
merged_df = pd.merge(merged_df, film_df.drop(columns=["last_update"], errors="ignore"), on="film_id", how="inner")

# Step 3: Aggregate - count customers per country
agg_df = (
    merged_df.groupby("country", as_index=False)
    .agg({"customer_id": "nunique"})
    .rename(columns={"customer_id": "customer_count"})
)

# Step 4: Order results (descending by customer count)
agg_df = agg_df.sort_values(by="customer_count", ascending=False)
agg_df = agg_df.set_index("country")

print(agg_df)


# Step 1: Merge film and inventory
merged_df1 = pd.merge(film_df, inventory_df.drop(columns=["last_update"], errors="ignore"), on="film_id", how="inner")
merged_df1 = pd.merge(merged_df, rental_df, on="inventory_id", how="inner")
merged_df1 = pd.merge(merged_df, payment_df.drop(columns=["last_update"], errors="ignore"), on="rental_id", how="inner")
# Step 3: Aggregate - count customers per country
agg_df1 = (
    merged_df1.groupby("title", as_index=False)
    .agg({"amount": "sum"})
    .rename(columns={"amount": "total_revenue"})
)
# Step 4: Order results (descending by customer count)
agg_df1 = agg_df1.sort_values(by="total_revenue", ascending=False)
print(agg_df1)


# streamlit
st.title("BluckBoster Entertainment")
st.header("Top Ten Country per Customer")


st.bar_chart(agg_df.head(10).set_index("country"))


st.header("Top Ten Films Generated Highest Revenue")


fig = px.bar(
    agg_df1.head(10),
    x="total_revenue",
    y="title",
    color="title"
)

fig.update_layout(
    showlegend=False
)

st.plotly_chart(fig)
