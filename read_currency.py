from pathlib import Path

class Forex_currency:

    # the path here will need
    forex_file = "physical_currency_list.csv"
    curr_dict = {}

    def __init__(self):
        self.data = []

        # finding the path to the csv file
        file_path = Path(__file__).parent.resolve() / self.forex_file
        # opening the file for reading
        f = open( file_path, "r" )
        # reading line by line
        for x in f:
            temp = x.strip().split(",")
            self.curr_dict[ temp[0] ] = temp[1]

    def get_forex_symbol( self ):
        return self.curr_dict.keys()

    def get_forex_currency( self ):
        return self.curr_dict

    def get_country( self ):
        return self.curr_dict.values()


