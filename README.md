### Trader Behavior Insights
Exploring the Relationship Between Market Sentiment and Trading Performance
Project Overview

This project analyzes the relationship between Bitcoin market sentiment (Fear & Greed Index) and trader performance using historical trading data from Hyperliquid.

The goal is to identify patterns in trader profitability and behavior under different market sentiment conditions and derive insights that could support smarter trading strategies.

### Datasets Used
1️⃣ Historical Trader Data (Hyperliquid)

Contains detailed trading activity such as:

Account

Coin / Symbol

Execution price

Trade size

Side (BUY / SELL)

Closed PnL

Timestamp

This dataset represents real trading behavior from market participants.

### 2️⃣ Bitcoin Fear & Greed Index

This dataset provides daily sentiment signals for the cryptocurrency market.

Columns include:

Date

Sentiment value

Sentiment classification

Possible sentiment categories:

Fear

Neutral

Greed

Extreme Greed

### Project Workflow

The analysis follows these steps:

1. Data Loading

Datasets were loaded using Pandas.

2. Data Cleaning

Converted timestamps to datetime format.

Created a common date column.

3. Data Merging

Trading data was merged with sentiment data based on the date field.

4. Data Analysis

Key analyses performed:

Average trader profit by market sentiment

Trading behavior (BUY vs SELL) under different sentiments

5. Visualization

Charts were created to illustrate relationships between:

Market sentiment and profit

Market sentiment and trade direction

### Key Insights
### 1️⃣ Trader Profitability vs Market Sentiment
Sentiment	Average Profit
Greed	87.89
Fear	50.04
Extreme Greed	25.41
Neutral	22.23

Insight

Traders achieved the highest profitability during Greed market conditions, suggesting strong performance during bullish trends.

### 2️⃣ Trading Behavior by Market Sentiment
Sentiment	BUY Trades	SELL Trades
Fear	66081	67790
Greed	15421	20868
Extreme Greed	3371	3591

Insight

Trading activity increases significantly during Fear periods, likely due to increased volatility and market uncertainty.

Visualizations

The project generates the following charts:

Trader Profit vs Market Sentiment

Long vs Short Positions by Sentiment

Charts are saved in:

outputs/charts/
### Technologies Used

Python

Pandas

Matplotlib

Seaborn

Git

GitHub

### Project Structure
Trader-Behavior-Insights
│
├── data
│   ├── historical_data.csv
│   └── fear_greed_index.csv
│
├── outputs
│   └── charts
│
├── analysis.py
├── README.md
└── requirements.txt
Installation & Usage

### Clone the repository:

git clone https://github.com/YOUR_USERNAME/Trader-Behavior-Insights.git

Navigate into the project:

cd Trader-Behavior-Insights

Install dependencies:

pip install -r requirements.txt

Run the analysis:

python analysis.py

Machine learning models to predict profitable trading conditions
