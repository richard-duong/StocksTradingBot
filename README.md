# StocksTradingBot
A trading bot I'm building for fun in python using polygon.io's stocks API.
<br><br><br>


## Prerequisites
* [Python >= 3.8](https://www.python.org/downloads/)
* [Pip](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
* [Python Virtual Environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
<br><br>

### Check your prerequisites with the following commands
For Python >= 3.8:
* `python3 --version` or
* `python --version`

For pip: 
* `pip3 --version` or
* `python3 -m pip --version`

For venv:
* `python3 -m venv --help`
<br><br>


## First Time Setup
1. Move to project directory `cd StocksTradingBot`
2. Run `./setup.sh` to setup the virtual environment and secrets file
3. Create a free API key on [polygon.io](https://polygon.io/) to use their API calls
4. Open the `.env` file and fill in your API key like this: `SECRET_API_KEY = "put your api key here"`
5. Source the virtual environment each time afterward with `source venv/bin/activate`
6. You're done! Feel free to run whatever scripts are available.