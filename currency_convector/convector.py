import requests


url = 'https://v6.exchangerate-api.com/v6/5124037e4fcf9900ebb0a843/latest/USD'
currencies = requests.get(url).json()


def convert(from_currency: str, to_currency: str, amount: float) -> float:
    """Function converts a currency.

        Args:
            from_currency (str): Currency of conversion from
            to_currency (str): Currency of conversion to
            amount (float): Amount of money to convert

        Returns:
            float: Converted amount

    """
    rates = currencies.get('conversion_rates')

    if from_currency != 'USD':
        amount = amount / rates.get(from_currency)
    output_amount = round(amount * rates.get(to_currency), 2)
    return output_amount
