try:
    from forex import name_list
    from forex import code_list
    from forex import forex_list
    print("Please enter the price in USD of your desired product: ")
   
    from decimal import *
    def line():
        print("--------------------------------------------------------------------------------")


    x = input()
    l = []
    def try_price(x):
        try:
            f = Decimal(x)
            l.append(f)
        except InvalidOperation:
            print("Invalid price, pleae enter a new price: ")
            x = input()
            try_price(x)
    try_price(x)

    print("What country would you like to see the price of this product in?")
    line()
    print(" 0. Australia", "\n"
    , "1. China", "\n"
    , "2. Britain", "\n"
    , "3. Japan", "\n"
    , "4. Russia")
    print("Please enter the number for your desired country.")
    h = 0
    def check_value(h):
        try:
            y = int(input())
            check_code(y)
        except ValueError:
            print("Code is invalid, please enter a new number: ")
            check_value(h)

    def check_code(y):
        if y > 4:
            print("Code is invalid, please enter a new number: ")
            check_value(h)
        else:
            q = forex_list[y]
            d = Decimal(q)
            line()
            z = l[0] * d
            print("The price of your product in ",name_list[y], "is", z , "!")
    check_value(h)
except:
    print("Please wait 1 minute, then run interface again :)") 