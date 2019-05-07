#!/usr/bin/python
print("Starting Coin Acceptor")

import RPi.GPIO as GPIO
from PoemGenerator import *
from thermalprinter import *
import time


pinCoin = 36
pinLed = 40
threshold = 0.25

lastTime = time.time()
coinOn = False

GPIO.setmode(GPIO.BOARD);
GPIO.setup(pinCoin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinLed, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(pinCoin, GPIO.RISING)

printer = ThermalPrinter(port='/dev/serial0', baudrate=9600)

# Number of pulses that the CoinAcceptor sends for each type of coin
# Lower number of pulses makes system recognize coins faster
# If you program the coin acceptor to emit one pulse per cent, it won't be very efficient
# coinPulses = {1 : 1, 2 : 5, 3 : 10, 4 : 25}
coinPulses = {1 : 1, 5 : 5, 10 : 10, 25 : 25}

# Defining how long the poem will be.
# Directly proportional to coin value:
wordsPerCent = 10
coinWords = {}
for item in coinPulses.items():
    coinWords[item[0]] = item[0] * wordsPerCent

# Manually adjusted
#coinWords = {1 : 20, 5 : 50, 10 : 80, 25: 125}

print('Ready to work...')
while True:
    if GPIO.event_detected(pinCoin):
        if(time.time() - lastTime < threshold):
            coinVal += 1
        else:
            coinOn = True
            coinVal = 1
            print('Coin inserted')

        lastTime = time.time()

    if (coinOn is True) & (time.time() - lastTime >= threshold):
        print('The value of the coin is '+ str(coinPulses[coinVal]))
        coinOn = False
        print("Generating poem... "+ str(time.time()))
        GPIO.output(pinLed, True)
        poem = generatePoem(coinPulses[coinVal])
        print("\n\n")
        print(poem)
        printer.out(poem)
        printer.feed(5)
        print("\n\n")
        print("Poem done... "+ str(time.time()))
        GPIO.output(pinLed, False)
