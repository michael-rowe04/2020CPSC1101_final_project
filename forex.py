import requests
import json
from read_currency import Forex_currency
from ForexClass import Forex
# read all the currency symbol from the file
forex_curr = Forex_currency()
forex_symbols = forex_curr.get_forex_symbol()
country = forex_curr.get_country()
#foreX = Forex.get_forex()
#forex_val = ForeX.forex
# the method below technically works but ... there is a limit of 5 requests per minute to Alphavantage
# I suggest you to keep only 5 currency symbols and remove all the others from the file physical_currency_list.csv
forex_d = {}

for symbol in forex_symbols:
    response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=" + 
    symbol + "&apikey=FEZI3YFJCLJOGMXN")
    raw_data = json.loads(response.text)
    
    
    # retreiving all forex
    forex_d[symbol] = Forex(str(raw_data["Realtime Currency Exchange Rate"]["4. To_Currency Name"]), str(raw_data["Realtime Currency Exchange Rate"]["3. To_Currency Code"]), str(raw_data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]))

name_list = []
for symbol in forex_d.values():
    name_list.append(symbol.get_curr_name())

code_list = []
for symbol in forex_d.values():
    code_list.append(symbol.get_curr_code())

forex_list = []
for symbol in forex_d.values():
    forex_list.append(symbol.get_forex())



    
    

'''     
def forex_list():
    l = []
    for symbol in forex_symbols:
        response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=" + 
        symbol + "&apikey=FEZI3YFJCLJOGMXN")
        raw_data = json.loads(response.text)
        foreX = str(raw_data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        l.append(foreX)
    return l   
print(forex_list())
        #else:
        #print("Invalid country code, please enter a new code: ")
    #def get_forex():        
        #for symbol in forex_d:
            #return symbol.forex



def country_name(symbol):
    for symbol in forex_symbols():
        curr
country_name()
'''
