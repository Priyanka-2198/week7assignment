import pandas as pd

# Load dataset
sales_df = pd.read_csv('data_sales.csv')

# Display sample data
print("\n📋 Sales Data Sample")
print("=" * 50)
print(sales_df.head())
sales_df['Total_Sale'] = pd.to_numeric(sales_df['Total_Sale'], errors='coerce')

regional_summary = sales_df.groupby('Region').agg(
    Total_Sales=('Total_Sale', 'sum'),
    Average_Sale=('Total_Sale', 'mean'),
    Number_of_Transactions=('Total_Sale', 'count')
).reset_index()

regional_summary['Average_Sale'] = regional_summary['Average_Sale'].round(2)

best_region = regional_summary.loc[
    regional_summary['Total_Sales'].idxmax()
]


regional_summary = regional_summary.sort_values(by='Total_Sales', ascending=False)

# Final output
print("\n📊 Sales Performance by Region")
print("=" * 60)
print(regional_summary)

print("\n🏆 Best Performing Region")
print("=" * 60)
print(f"Region: {best_region['Region']}")
print(f"Total Sales: {best_region['Total_Sales']:.2f}")
print(f"Average Sale: {best_region['Average_Sale']:.2f}")
print(f"Transactions: {best_region['Number_of_Transactions']}")

# Business Insights
print("\n📌 Business Insights")
print("=" * 60)
print(f"- The best performing region is {best_region['Region']} based on total sales.")
print("- Regions with higher average sales indicate stronger customer spending.")
print("- Management can focus on low-performing regions to improve revenue.")
print("- This report helps in identifying sales trends across regions.")