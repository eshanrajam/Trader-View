# Stock Data Viewer 📈  

A Python script that fetches, analyzes, and displays stock/ETF data using Yahoo Finance (`yfinance`).  
This tool calculates **Relative Strength Index (RSI)** and **Relative Vigor Index (RVI)** to help with stock trend analysis.  

---

## 🚀 Features  

✅ Fetch **historical** stock/ETF data using `yfinance`  
✅ Calculate **RSI (Relative Strength Index)** for momentum analysis  
✅ Calculate **RVI (Relative Vigor Index)** for trend confirmation  
✅ Retrieve **live** stock opening and current prices  
✅ Display formatted stock data in a **table** (`tabulate` library)  
✅ Save stock data as a **CSV file** for further analysis  
✅ **Error handling & logging** for smooth execution  

---

## 🛠 Installation  

### **1️⃣ Install Python (if not installed)**  
Download and install Python from [python.org](https://www.python.org/downloads/).  

### **2️⃣ Install Dependencies**  
Run the following command to install the required Python libraries:  
pip install yfinance pandas tabulate

1️⃣ Run the script using:
python stock_data_viewer.py
2️⃣ Enter a stock or ETF ticker symbol (e.g., AAPL for Apple, SPY for S&P 500 ETF).

3️⃣ Enter the start date (YYYY-MM-DD format) to fetch historical data.

4️⃣ The script will:

Fetch historical stock data

Calculate RSI and RVI

Display the data in a table format

Fetch live stock prices and calculate price change

5️⃣ (Optional) Save the stock data to a CSV file.

6️⃣ Choose whether to analyze another stock or exit.


📝 How It Works
📌 RSI Calculation
Measures momentum by comparing average gains vs. losses over 14 periods.

Values above 70 indicate an overbought market.

Values below 30 indicate an oversold market.

📌 RVI Calculation
Compares stock's opening-to-closing movement to its high-to-low range.

Values above 0 suggest bullish trends.

Values below 0 suggest bearish trends.


💾 Saving Data
To save the stock data to a CSV file, enter "yes" when prompted:
Do you want to save this data to a CSV file? (yes/no): yes
Data saved to AAPL_from_2024-01-01.csv


🛠 Troubleshooting
1️⃣ Getting an error fetching data?

Ensure the ticker symbol is correct.

Make sure the start date is in YYYY-MM-DD format.

2️⃣ RSI or RVI values are NaN?

The script requires at least 14 days of data for accurate calculations.

3️⃣ No live data?

The market may be closed. Try again during trading hours.


Happy Trading! 📊🚀
