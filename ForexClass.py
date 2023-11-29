class Forex:
    '''to_currency_name = "4. To_Currency Name"
    to_currency_code = "3. To_Currency Code"
    forex = "5. Exchange Rate"
    '''
    def __init__(self, to_currency_name, to_currency_code, forex):
        self.to_currency_name = to_currency_name
        self.to_currency_code = to_currency_code
        self.forex = forex
    
    
    def print_forex_info(self):
        print("To currency: " + self.to_currency_name +
        "\n Currency code: " + self.to_currency_code + 
        "\n Forex: " + self.forex)

    def get_forex(self):
        return self.forex

    def get_curr_name(self):
        return self.to_currency_name

    def get_curr_code(self):
        return self.to_currency_code

   
        