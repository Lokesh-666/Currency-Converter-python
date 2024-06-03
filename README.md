# Currency Converter Program

This is a simple currency converter program implemented in Python. It allows the user to convert an amount from one currency to another using real-time exchange rates provided by the `forex-python` library.

## Features

- Convert an amount from one currency to another.
- User-friendly prompts for input.
- Displays the converted amount rounded to two decimal places.

## Requirements

To run this program, you need to have Python installed on your system. Additionally, the program requires the `forex-python` library for fetching real-time exchange rates.

## Installation

1. **Install Python:**

   Make sure you have Python installed. You can download and install Python from the official website: [Python.org](https://www.python.org/downloads/).

   To check if Python is already installed, you can run the following command in your terminal or command prompt:

   ```sh
   python --version
   ```

   or

   ```sh
   python3 --version
   ```

2. **Install `forex-python` library:**

   You need to install the `forex-python` library to fetch real-time exchange rates. You can install it using pip:

   ```sh
   pip install forex-python
   ```

3. **Download the Code:**

   Clone or download this repository to your local machine.

   ```sh
   git clone https://github.com/yourusername/currency-converter.git
   ```

   Navigate to the directory where you have saved the code.

   ```sh
   cd currency-converter
   ```

## How to Run the Program

1. Open your terminal or command prompt.
2. Navigate to the directory where the code is saved.
3. Run the following command to start the program:

   ```sh
   python currency_converter.py
   ```

   or

   ```sh
   python3 currency_converter.py
   ```

## Usage

1. When the program starts, it will ask if you wish to use the currency converter.
2. Enter 'Y' for yes or 'N' for no.
3. If you choose 'Y', follow the prompts to:
   - Enter the amount you wish to convert.
   - Enter the currency you wish to convert to (e.g., USD, EUR).
   - Enter the currency you wish to convert from (e.g., USD, EUR).
4. The program will display the converted amount.
5. If you choose 'N', the program will exit with a goodbye message.
6. If you enter any other input, the program will prompt you to enter 'Y' or 'N'.

## Example

```
Do you wish to use this Currency Converter:
Y/N?: Y
Welcome to the Currency Converter!
Please enter the amount you wish to convert:
100
Please enter the currency you wish to convert to:
EUR
Please enter the currency you wish to convert from:
USD
90.50
Thank you for using the Currency Converter!
Have a nice day!

Do you wish to use this Currency Converter:
Y/N?: N
No Problem!!
Good Day!!
```

## Notes

- Ensure you have an active internet connection to fetch the latest exchange rates.
- The currency codes must be entered in their standard ISO 4217 format (e.g., USD, EUR, GBP).

## Contributing

If you find any bugs or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License.
