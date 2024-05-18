class Ethereum:
    def __init__(self, name, value, market_cap):
        self.name = name
        self.value = value
        self.market_cap = market_cap

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getMarketCap(self):
        return self.market_cap