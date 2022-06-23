from dotenv import load_dotenv
import os

load_dotenv()
print(f"Your api key is: {os.environ.get('SECRET_API_KEY')}")
