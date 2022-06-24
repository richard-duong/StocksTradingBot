import sys
sys.path.append(".")  # gives visibility for modules in parent folder
sys.path.append("../")  # gives visibility for modules in parent folder

# custom imports
from StocksAPI import StarterStockBot

bot = StarterStockBot()
client = bot.client
financials = client.get_ticker_details("NFLX")
print(financials)

for (i, n) in enumerate(client.list_ticker_news("INTC", limit=5)):
   print(i, n)
   if i == 5:
       break




