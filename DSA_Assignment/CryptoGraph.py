import csv
import _pickle as cPickle 
import DSAGraph as graph
import AssetClass as Asset
import DSALinkedList as linkedList
import sys
from re import sub
from decimal import Decimal

max_rec = 0x100000
sys.setrecursionlimit(max_rec)

def main():
    assetGraph = loadData()
    loadTradeInfo(assetGraph)

    menu(assetGraph)


def menu(assetGraph):
    option = 0

    print("Menu!")
    print("Please select an option: \n")

    while(option != 8):
        print("1: Display assest details\n2: Display trade details\n3: Find trade paths\n4: Set asset filter\n5: Asset overview\n6: Trade overview\n7: Save data\n8: Exit\n")
        option = int(input())

        if(option == 1):
            print("Displaying asset details\n")
            for node in assetGraph.linkedList:
                node.value.printDetails()

        elif(option == 2):
            print("Displaying trade details\n")
            loadTradePaths()

        elif(option == 3):
            print("Display trade paths\n")
            assetGraph.display()

        elif(option == 4):
            print("Setting asset filter\n")

        elif(option == 5):
            print("Asset overview")
            assetOverview(assetGraph)

        elif(option == 6):
            print("Trade overview\n")
            tradeOverview(assetGraph)

        elif(option == 7):
            print("Saving data\n")
            if(assetGraph != None):
                saveFile(assetGraph)
            else:
                print("Graph has no data")

    print("Exit!")

def loadData():
    print("Loading data!\n")
    file = open("asset_info.csv", "r")
    reader = csv.reader(file)
    next(reader, None)  
    retGraph = graph.DSAGraph()

    rank = []
    name = []
    symbol = []
    price = []

    for row in reader:
        rank.append(row[0])
        name.append(row[1])
        symbol.append(row[2])
        price.append(row[5])

    for x in range(len(rank)):

        temp = Asset.Asset(rank[x], name[x], symbol[x], price[x])
        retGraph.add_node(temp)

    file.close()
    return retGraph

def loadTradeInfo(graph):
    print("Loading trade info!\n")
    file = open("trade_prices.csv", "r")
    reader = csv.reader(file)
    next(reader, None) 

    symbol1 = []
    symbol2 = []

    temp1 = None
    temp2 = None

    for row in reader:
        symbol1.append(row[1])
        symbol2.append(row[2])

    for x in range (len(symbol1)):
        for node in graph.linkedList:
            if(symbol1[x] == node.value.getSymbol()):
                temp1 = node.value
                for item in graph.linkedList:
                    if(symbol2[x] == item.value.getSymbol()):
                        temp2 = item.value

        graph.add_edge(temp1, temp2)

    file.close()

def loadTradePaths():
    file = open("trade_prices.csv", "r")
    reader = csv.reader(file)
    retGraph = graph.DSAGraph()

    symbol = []

    for row in reader:
        symbol.append(row[0])

    for x in range (len(symbol)):
        print(symbol[x])

    file.close()

def setAssetFilter(graph):
    tempSymbol = ""
    while(tempSymbol != "x"):
        tempSymbol = input("Please type a valid asset symbol or type x to exit")
        for node in graph.linkedList:
            if(node.value.symbol == tempSymbol):
                node.toString()


def assetOverview(graph):
    print("Prices under $1: ")
    for node in graph.linkedList:
        tempPrice = Decimal(sub(r'[^\d.]', '', node.value.getPrice()))
        if tempPrice < 0.1:
            print(node.value.getName(),":", node.value.getPrice())

def tradeOverview(graph):
    print("The trade count is ", graph.count,"\n")

def saveFile(myObject):
    print("Saving Object to File...")
    try:
        with open("graph.pickle", "wb") as dataFile:
            cPickle.dump(myObject, dataFile)
            print("File saved\n")
    except:
            print("Error: problem pickling object!\n")


main()
