# https://www.hackerrank.com/challenges/birthday-cake-candles/problem


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    tallest_candle = max(ar)
    number_of_tallest_candles = 0
    for candle in ar:
        if candle == tallest_candle:
            number_of_tallest_candles += 1

    return number_of_tallest_candles
