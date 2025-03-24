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
