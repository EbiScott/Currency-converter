#My Python script to convert currencies in realtime

from forex_python.converter import CurrencyRates

def converter(amount, original_currency, final_currency):
    currency = CurrencyRates()
    rate = currency.get_rate(original_currency, final_currency)
    result = amount * rate
    return result

# Example usage
original_currency = input("Enter the original currency: ").upper()
final_currency = input("Enter the final currency: ").upper()
amount = float(input("Enter the amount: "))

try:
    answer = converter(amount, original_currency, final_currency)
    print(f"{amount} {original_currency} is equal to {answer:.2f} {final_currency}")
except Exception as e:
    print(f"Error: {e}")

