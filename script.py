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

def printCurrencyNames():
     print('USD')
     print('IDR')
     print('BGN')
     print('ILS')
     print('GBP')
     print('DKK')
     print('CAD')
     print('JPY')
     print('HUF')
     print('RON')
     print('MYR')
     print('SEK')
     print('SGD')
     print('HKD')
     print('AUD')
     print('CHF')
     print('KRW')
     print('CNY')
     print('TRY')
     print('HRK')
     print('NZD')
     print('THB')
     print('EUR')
     print('NOK')
     print('RUB')
     print('INR')
     print('MXN')
     print('CZK')
     print('BRL')
     print('PLN')
     print('PHP')
     print('ZAR')

def main():
    # while(1):
        print("Do you wish to use this Currency Converter: ")
        answer = input("Y/N?: ")
        if answer.upper() == "Y" :
            print("Welcome to the Currency Converter! ")
            print("Please enter the amount you wish to convert: ")
            amount = float(input())
            print("Here are the list of all currencies and their acronyms: ")
            printCurrencyNames()
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