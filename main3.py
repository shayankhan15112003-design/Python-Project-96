class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def set_max_price(self, price):
        self.__maxprice = price
import time

c = Computer()

c.sell()
time.sleep(1)
c.__maxprice = 1000
c.sell()
time.sleep(1)
c.set_max_price(1000)
c.sell()