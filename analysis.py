import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
trader = pd.read_csv("data/historical_data.csv")
sentiment = pd.read_csv("data/fear_greed_index.csv")

print("Trader Data Preview:")
print(trader.head())

print("\nSentiment Data Preview:")
print(sentiment.head())

# Convert timestamp
trader["Timestamp"] = pd.to_datetime(trader["Timestamp"], unit="ms")

# Create date column
trader["date"] = trader["Timestamp"].dt.date
sentiment["date"] = pd.to_datetime(sentiment["date"]).dt.date

# Merge datasets
merged = pd.merge(trader, sentiment, on="date", how="left")

print("\nMerged Data Preview:")
print(merged.head())

# Profit analysis
profit_by_sentiment = merged.groupby("classification")["Closed PnL"].mean()
print("\nAverage Profit by Sentiment:")
print(profit_by_sentiment)

# Long vs Short analysis
side_analysis = merged.groupby(["classification","Side"]).size()
print("\nLong vs Short by Sentiment:")
print(side_analysis)

# Chart 1
plt.figure()
sns.boxplot(x="classification", y="Closed PnL", data=merged)
plt.title("Trader Profit vs Market Sentiment")
plt.savefig("outputs/charts/profit_vs_sentiment.png")
plt.close()

# Chart 2
plt.figure()
sns.countplot(x="classification", hue="Side", data=merged)
plt.title("Long vs Short Positions by Sentiment")
plt.savefig("outputs/charts/long_short_sentiment.png")
plt.close()

print("\nCharts saved in outputs/charts folder")