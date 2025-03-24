import yfinance as yf
import pandas as pd
from tabulate import tabulate
import logging

# Set up logging for better error tracking
logging.basicConfig(filename="stock_data.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

# Adjust pandas display settings for better console output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

class StockDataFetcher:
    """
    A class to fetch and process stock data, including calculating RSI and RVI indicators.
    """

    def __init__(self, symbol, start_date):
        """
        Initialize the StockDataFetcher with a stock symbol and start date.
        """
        self.symbol = symbol.upper()
        self.start_date = start_date
        self.data = None
        self.live_open_price = None
        self.live_price = None

    def fetch_data(self):
        """
        Fetch historical stock data using yfinance.
        """
        try:
            stock = yf.Ticker(self.symbol)
            self.data = stock.history(start=self.start_date)

            if self.data.empty:
                raise ValueError(f"No data found for {self.symbol} from {self.start_date} to current date. "
                                 "Check the ticker symbol and date range.")

            self.data = self.data[['Open', 'High', 'Low', 'Close']]

        except Exception as e:
            logging.error(f"Error fetching data for {self.symbol}: {e}")
            raise ValueError(f"Failed to fetch data for {self.symbol}. Please try again.")

    def calculate_rsi(self, period=14):
        """
        Calculate the Relative Strength Index (RSI) using an exponential moving average.
        """
        delta = self.data['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.ewm(span=period, adjust=False).mean()
        avg_loss = loss.ewm(span=period, adjust=False).mean()

        rs = avg_gain / avg_loss
        self.data['RSI'] = 100 - (100 / (1 + rs))

    def calculate_rvi(self, period=14):
        """
        Calculate the Relative Vigor Index (RVI).
        """
        close_open_diff = self.data['Close'] - self.data['Open']
        high_low_diff = self.data['High'] - self.data['Low']

        rvi_numerator = close_open_diff.rolling(window=period).mean()
        rvi_denominator = high_low_diff.rolling(window=period).mean()

        self.data['RVI'] = rvi_numerator / rvi_denominator

    def get_live_data(self):
        """
        Fetch the live opening and current price of the stock.
        """
        try:
            stock = yf.Ticker(self.symbol)
            live_data = stock.history(period="1d")

            if not live_data.empty:
                self.live_open_price = live_data['Open'].iloc[-1]
                self.live_price = live_data['Close'].iloc[-1]
            else:
                raise ValueError(f"Live price data for {self.symbol} is unavailable.")

        except Exception as e:
            logging.error(f"Error fetching live data for {self.symbol}: {e}")
            self.live_open_price, self.live_price = None, None

    def calculate_live_change(self):
        """
        Calculate the live percentage change and price difference compared to the opening price.
        """
        if self.live_open_price is not None and self.live_price is not None:
            price_diff = self.live_price - self.live_open_price
            percent_change = (price_diff / self.live_open_price) * 100
            arrow = "↑" if price_diff > 0 else "↓" if price_diff < 0 else "→"

            return price_diff, percent_change, arrow
        return None, None, None

    def display_data(self):
        """
        Display stock data in a table format.
        """
        print(f"\nStock data for {self.symbol} from {self.start_date} to current date:")

        # Create a formatted DataFrame for display (so it doesn't affect CSV saving)
        display_df = self.data.copy()
        display_df['Open'] = display_df['Open'].round(2).apply(lambda x: f"${x:,.2f}")
        display_df['High'] = display_df['High'].round(2).apply(lambda x: f"${x:,.2f}")
        display_df['Low'] = display_df['Low'].round(2).apply(lambda x: f"${x:,.2f}")
        display_df['Close'] = display_df['Close'].round(2).apply(lambda x: f"${x:,.2f}")
        display_df['RSI'] = display_df['RSI'].round(2)
        display_df['RVI'] = display_df['RVI'].round(4)

        table_data = display_df.reset_index().values.tolist()
        headers = display_df.reset_index().columns.tolist()

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

        # Display live data
        price_diff, percent_change, arrow = self.calculate_live_change()
        if price_diff is not None:
            print(f"\nLive Data for {self.symbol}:")
            print(f"  Opening Price: ${self.live_open_price:.2f}")
            print(f"  Current Price: ${self.live_price:.2f}")
            print(f"  Price Change: ${price_diff:.2f} {arrow}")
            print(f"  Percent Change: {percent_change:.2f}% {arrow}")

    def save_to_csv(self, filename=None):
        """
        Save stock data to a CSV file.
        """
        if filename is None:
            filename = f"{self.symbol}_from_{self.start_date}.csv"
        self.data.to_csv(filename)
        print(f"Data saved to {filename}")

def main():
    while True:
        stock_symbol = input("Enter the stock or ETF ticker symbol (e.g., AAPL for Apple, SPY for S&P 500 ETF): ").strip()
        start_date_input = input("Enter the start date (YYYY-MM-DD): ").strip()

        try:
            fetcher = StockDataFetcher(stock_symbol, start_date_input)
            fetcher.get_live_data()
            fetcher.fetch_data()
            fetcher.calculate_rsi()
            fetcher.calculate_rvi()
            fetcher.display_data()

            save_data = input("\nDo you want to save this data to a CSV file? (yes/no): ").strip().lower()
            if save_data == 'yes':
                fetcher.save_to_csv()

        except ValueError as ve:
            print(f"Error: {ve}")
            logging.error(ve)
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            logging.error(e)

        another_stock = input("\nWould you like to analyze another stock or ETF? (yes/no): ").strip().lower()
        if another_stock != 'yes':
            print("Thank you for using the stock data viewer. Goodbye!")
            break

if __name__ == "__main__":
    main()

