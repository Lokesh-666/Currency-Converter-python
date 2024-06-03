from forex_python.converter import CurrencyRates

converter = CurrencyRates()
# Currency Converting function, given amount, currency conversion from and to
def converterFunction(amount, currency_to, currency_from):
    currency_to = str(currency_to).upper()
    currency_from = str(currency_from).upper()
    amount = float(amount)
    rate = converter.get_rate(currency_from, currency_to)
    converted_amount = round(amount * rate, 2)
    return converted_amount
    
def main():
    # while(1):
        print("Do you wish to use this Currency Converter: ")
        answer = input("Y/N?: ")
        if answer.upper() == "Y" :
            print("Welcome to the Currency Converter! ")
            print("Please enter the amount you wish to convert: ")
            amount = float(input())
            print("Please enter the currency you wish to convert to: ")
            currency_to = str(input())  
            print("Please enter the currency you wish to convert from: ")
            currency_from = str(input())
            print(converterFunction(amount, currency_to, currency_from))
            print("Thank you for using the Currency Converter! ")
            print("Have a nice day! ")
        elif answer.upper() == "N":
            print("No Problem!!")
            print("Good Day!!")
            # break
        else:
            print("Please enter Y or N")

if __name__ == '__main__':
    main()