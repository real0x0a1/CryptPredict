# CryptPredict

## Overview
CryptPredict is a Python project that aims to predict cryptocurrency prices using linear regression. The project utilizes the Binance exchange API to fetch historical price data, prepares the data for model training, and employs a linear regression model to make predictions for future prices.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Real0x0a1/CryptPredict.git
   cd CryptPredict
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure you have a Binance API key and secret. Update the `ccxt.binance()` initialization in the code with your credentials.

2. Run the script:
   ```bash
   python CryptPredict.py
   ```

3. View the predicted prices for the specified cryptocurrency in the console.

## Configuration
- Adjust the `symbol` variable to the cryptocurrency pair you want to predict (e.g., 'BTC/USDT').
- Modify the `start_date` variable to set the beginning of the historical data.
- Customize the number of `future_days` for the prediction horizon.

## Dependencies
- [ccxt](https://github.com/ccxt/ccxt): A cryptocurrency trading library providing unified APIs across various exchanges.
- [numpy](https://numpy.org/): A library for numerical computations in Python.
- [scikit-learn](https://scikit-learn.org/): A machine learning library for simple and efficient tools for data analysis.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the project.

## Author
- Ali (Real0x0a1)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
