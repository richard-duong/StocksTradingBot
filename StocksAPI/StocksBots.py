import os
from dotenv import load_dotenv
from polygon import RESTClient

ENV_KEY='POLYGON_API_KEY'
load_dotenv()

class FreeStockBot:
	# static class client (is this multithread safe?)	
	__secret = os.environ.get(ENV_KEY)
	print(__secret)
	client = RESTClient(api_key = __secret)

	# not sure what to put here yet
	def __init__(self):
		return
		
class StarterStockBot(FreeStockBot):
	def __init__(self):
		super().__init__()