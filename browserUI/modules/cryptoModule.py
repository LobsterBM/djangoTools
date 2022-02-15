
import requests
import time


class Coin:
    def __init__(self, name , symbol , price , previous , dayMax , dayMin , priceChange ):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.previous = previous
        self.dayMax = dayMax
        self.dayMin = dayMin
        self.priceChange = priceChange
        self.color = ["grey", "on_green"]
        if priceChange > 0 :
            self.colorPercent = ["grey", "on_green"]
        else :
            self.colorPercent = ["yellow", 'on_red']

    def updatePrice(self, price, priceChange):
        if price != self.price:
            self.previous = self.price
            self.price = price
            if(self.previous > self.price):
                self.color = ["yellow", 'on_red']
            else:
                self.color = ["grey", "on_green"]
        self.priceChange = priceChange
        if priceChange > 0:
            self.colorPercent = ["grey", "on_green"]
        else:
            self.colorPercent = ["yellow", 'on_red']


def cryptoPrint(settings, coins):
    tableTitle =[settings.FIAT]
    currentPrices =["Current : "]
    previousPrices = ["Previous : "]
    priceChanges = ["24h % : "]
    dayMaxes = ["24h max : "]
    dayMins = ["24h min : "]

    for i in coins:
        tableTitle.append(i.symbol.upper())
        currentPrices.append(colored(str(i.price), i.color[0], i.color[1],attrs=['bold']   ))
        previousPrices.append(str(i.previous))
        priceChanges.append(colored(str(i.priceChange),i.colorPercent[0], i.colorPercent[1],attrs=['bold']    ))
        dayMaxes.append(str(i.dayMax))
        dayMins.append(str(i.dayMin))

    completeTable =[]
    completeTable.append(tableTitle)
    completeTable.append(currentPrices)
    completeTable.append(previousPrices)
    completeTable.append(priceChanges)
    completeTable.append(dayMaxes)
    completeTable.append(dayMins)

    table_instance = terminaltables.SingleTable(completeTable, "Crypto-ticker : ")
    table_instance.justify_columns[1] = 'center'
    table_instance.justify_columns[2] = 'center'
    table_instance.justify_columns[3] = 'center'

    print(table_instance.table)
    print()




def printInterface(settings , crypto ,timer ,y,x ):
    url = settings.API_URL
    currency = settings.FIAT.lower()
    cryptoData = requests.get(url + currency).json()
    cryptoList = []
    for i in cryptoData:
        if i['symbol'].upper() in crypto:
            cryptoList.append(Coin(i['id'], i["symbol"], i["current_price"], 0, i["high_24h"], i["low_24h"],i["price_change_percentage_24h"]))


    while True :


        for i in cryptoData:
            if i['symbol'].upper() in crypto:
                for j in cryptoList:
                    if i['symbol'].upper() == j.symbol.upper():
                        j.updatePrice(i["current_price"],i['price_change_percentage_24h'])
        LOCK.acquire()
        move(y,x)
        cryptoPrint(cryptoList)
        LOCK.release()

        time.sleep(timer)
        cryptoData = None
        cryptoData = requests.get(url + currency).json()