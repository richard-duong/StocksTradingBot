from dotenv import load_dotenv
import os

load_dotenv()
ENV_KEY='POLYGON_API_KEY'
SECRET = os.environ.get(ENV_KEY)
print(SECRET)
print(f"Your api key is: {os.environ.get(ENV_KEY)}")
