from six.moves import configparser
from coinmarketcap import Market
from terminaltables import AsciiTable
from colorama import Fore, Back, Style
import six

config = configparser.ConfigParser()
config.read('config.ini')

headings = config.get("Table","headings")

coin_data = [
    config.get("Table","headings").split(","),
]

coinmarketcap = Market()
ticker = coinmarketcap.ticker(start=0, limit=12, convert='EUR')

def colorize(value, symbol = ''):
    state = Fore.RED if float(value) <= 0 else Fore.GREEN
    return state + value + symbol + Fore.RESET

for coin in ticker:
    coin_data.append([
        Fore.CYAN + coin['name'] + Fore.RESET ,
        coin['symbol'],
        coin['price_eur'],
        coin['price_btc'],
        colorize(coin['percent_change_1h'], '%'),
        colorize(coin['percent_change_24h'], '%'),
        colorize(coin['percent_change_7d'], '%')
    ])

table = AsciiTable(coin_data)
print(table.table)
