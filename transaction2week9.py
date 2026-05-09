import pandas as pd

# Load transaction data
transactions_df = pd.read_csv('transactions.csv')

# Convert Date column to datetime
transactions_df["Date"] = pd.to_datetime(
    transactions_df["Date"],
    dayfirst=True
)

# Clean Amount column
transactions_df["Amount"] = pd.to_numeric(
    transactions_df["Amount"]
    .astype(str)
    .replace('[\$,]', '', regex=True),
    errors='coerce'
)


# Practice Exercise 2.1: Spending Trend Analysis

# Create Day of Week column
transactions_df["DayOfWeek"] = transactions_df["Date"].dt.day_name()

# Spending by day of week
day_spending = transactions_df.groupby("DayOfWeek")["Amount"].sum()

print("Spending by Day of Week:")
print(day_spending)

# Daily spending trend
daily_spending = transactions_df.groupby("Date")["Amount"].sum()

print("\nDaily Spending Trend:")
print(daily_spending)

# High spending transactions
high_spending = transactions_df[
    transactions_df["Amount"] > 100
]

print("\nHigh Spending Transactions:")
print(high_spending)

# Practice Exercise 2.2: Budget Category Analysis

# Average spending by category
average_spending = transactions_df.groupby("Category")["Amount"].mean()

print("\nAverage Spending by Category:")
print(average_spending)

# Variation in spending
variation = transactions_df.groupby("Category")["Amount"].std()

print("\nVariation in Spending:")
print(variation)

# Suggested budget with 10% buffer
suggested_budget = average_spending * 1.10

print("\nSuggested Budget by Category:")
print(suggested_budget)

# Categories with highest spending
high_category_spending = (
    transactions_df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nHighest Spending Categories:")
print(high_category_spending)

print("\nAnalysis Completed Successfully ✅")