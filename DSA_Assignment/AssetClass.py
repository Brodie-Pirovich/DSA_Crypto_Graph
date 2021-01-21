class Asset:
    def __init__(self, inRank, inName, inSymbol, inPrice):
        self.rank = inRank
        self.name = inName
        self.symbol = inSymbol
        self.price = inPrice

    def getRank(self):
        return self.rank

    def getName(self):
        return self.name

    def getSymbol(self):
        return self.symbol

    def getPrice(self):
        return self.price

    def printDetails(self):
        print("Name:", self.name, "Rank:", self.rank, "Symbol:", self.symbol, "Price:", self.price,"\n")