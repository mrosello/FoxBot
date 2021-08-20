import websocket, json, pprint, talib
import numpy as np
import config
from binance.client import Client
from binance.enums import *

RSI_PERIOD = 14
RSI_OVERBOUGH = 72
RSI_OVERSOLD = 30

MACD_FASTPERIOD = 12
MACD_SLOWPERIOD = 26
MACD_SIGNALPERIOD = 9

TRADE_SYMBOL = 'ADABTC'
TRADE_QUANTITY = 13
TRADE_PERIOD = '3m'

SOCKET = "wss://stream.binance.com:9443/ws/" + TRADE_SYMBOL.lower() + "@kline_" + TRADE_PERIOD

# positions: 0 = not i position, 1 = half position, > 2 = full position
current_position = 0
uptrend = []
order_completed = []

client = Client(config.API_KEY, config.API_SECRET)

# closes initialization

closes = []

if TRADE_PERIOD == '1m':
    candlesticks = client.get_historical_klines(TRADE_SYMBOL, Client.KLINE_INTERVAL_1MINUTE, "35 mins ago UTC")
if TRADE_PERIOD == '3m':
    candlesticks = client.get_historical_klines(TRADE_SYMBOL, Client.KLINE_INTERVAL_3MINUTE, "2 hours ago UTC")
if TRADE_PERIOD == '5m':
    candlesticks = client.get_historical_klines(TRADE_SYMBOL, Client.KLINE_INTERVAL_3MINUTE, "8 hours ago UTC")

for candlestick in candlesticks:
    closes.append(float(candlestick[4]))

def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print("Sending order")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity, recvWindow=59000)
        print(order)
        return True
    except Exception as e:
        print("Order failed")
        return False

    return False

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws,message):
    global RSI_OVERBOUGH
    global RSI_OVERSOLD
    global RSI_PERIOD
    global closes
    global current_position

    json_message = json.loads(message)

    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("------ New candle ------")
        print("Candle closed at {}".format(close))
        closes.append(float(close))
        rsi = talib.RSI(np.array(closes), timeperiod=RSI_PERIOD)

        last_rsi = rsi[-1]
        print("the current rsi is {}".format(last_rsi))

        if last_rsi > RSI_OVERBOUGH:
            print("Overbough! Sell! Sell! Sell!")
            if current_position > 0:
                order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                if order_succeeded:
                    current_position = current_position - 1
                    print("Position sold")
            else:
                print("Overbought, but you are not in position")

        if last_rsi < RSI_OVERSOLD:
            print('Oversold! Buy! Buy! Buy!')
            if current_position < 2:
                order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                if order_succeeded:
                    current_position = current_position + 1
                    print("Position taken")
            else:
                print("You are already in position!")

ws = websocket.WebSocketApp(SOCKET, on_open=on_open , on_close=on_close , on_message=on_message)
ws.run_forever()