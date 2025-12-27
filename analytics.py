import yfinance as yf
import matplotlib.pyplot as plt

# Fetch Bitcoin data for last 30 days
btc = yf.download('BTC-USD', period='30d', interval='1d')

# Plot closing price
plt.figure()
plt.plot(btc.index, btc['Close'])
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Bitcoin (BTC-USD) Price - Last 30 Days')
plt.tight_layout()

# Save plot
plt.savefig('plot.png')
plt.close()