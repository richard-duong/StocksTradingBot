import os
from dotenv import load_dotenv
from polygon import RESTClient

ENV_KEY = "POLYGON_API_KEY"

class FreeStockBot:
	# static class client (is this multithread safe?)	
	__secret = str(os.environ.get(ENV_KEY))
	client = RESTClient(api_key = __secret)

	# not sure what to put here yet
	def __init__(self):
		return
		
class StarterStockBot(FreeStockBot):
	def __init__(self):
		FreeStockBot.__init__()