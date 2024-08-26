import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


def ReadCleanData(Filename):
    Data = pd.read_csv(Filename)
    Data.dropna(inplace = True)
    Data = Data[Data['Electric Range'] != 0]
    return Data

def ElectricRangeGraph(Data):
    Data['Electric Range'].plot(kind='hist',title='Electric Range')
    plt.show()

def OrganiseData(Data,Value,Num):
    DataCounts = Counter(Data[Value])
    Data = list(DataCounts.keys())
    Count = list(DataCounts.values())

    ModifiedData = []
    ModifiedCount = []
    OtherTotal = 0
    for cat, value in zip(Data, Count):
        if value < Num:
            OtherTotal += value
        else:
            ModifiedData.append(cat)
            ModifiedCount.append(value)
    if OtherTotal > 0:
        ModifiedData.append('Other')
        ModifiedCount.append(OtherTotal)
    return ModifiedCount,ModifiedData

def MarketPie(Data):
    Count,Makes = OrganiseData(Data,'Make',1000)

    fig, ax = plt.subplots(figsize=(10,8),subplot_kw=dict(aspect='equal'))
    wedges, texts, autotexts = plt.pie(Count,labels=Makes,startangle=90,autopct='%1.1f%%',counterclock=False)
    
    plt.title('Electric Car Makes Distribution')
    ax.legend(wedges, Makes, title='Makes',loc='center',bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts,size=8,weight='bold')
    plt.show()

def Averages(Data):    
    print('\nAverage Electric Range:',Data['Electric Range'].mean().round(2))
    print('Average Model Year:',int(Data['Model Year'].mean().round()))
    
def CityPie(Data):
    Count, Cities = OrganiseData(Data,'City',1500)

    fig1, ax1 = plt.subplots(figsize=(10,8),subplot_kw=dict(aspect='equal'))
    wedges1, texts1, autotexts1 = plt.pie(Count,labels=Cities,startangle=90,autopct='%1.1f%%',counterclock=False)
    
    plt.title('Electric Car City Distribution',pad=3)
    ax1.legend(wedges1, Cities, title='Cities',loc='upper right',bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts1,size=8,weight='bold')
    plt.show()

def ModelPie(Data):
    Count, Model = OrganiseData(Data,'Model',2300)

    fig1, ax1 = plt.subplots(figsize=(10,8),subplot_kw=dict(aspect='equal'))
    wedges1, texts1, autotexts1 = plt.pie(Count,labels=Model,startangle=90,autopct='%1.1f%%',counterclock=False)
    
    plt.title('Electric Car Models Distribution',pad=3)
    ax1.legend(wedges1, Model, title='Models',loc='upper right',bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts1,size=8,weight='bold')
    plt.show()

def AgeRangeGraph(Data):
    Data['Model Year'].plot(kind='hist',title='Model Year')
    plt.show()

def ShowMenu():
    print("\nMenu")
    print("1. Show electric range graph")
    print("2. Show market share pie chart")
    print("3. Show city distribution pie chart")
    print("4. Show car age range chart")
    print("5. Show model distribution pie chart")
    print("6. Get averages")
    print("6. Exit")


if __name__ == '__main__':
    plt.rcParams['figure.figsize'] = [13, 7]
    plt.rcParams.update({'font.size': 18})
    FileName = 'Electric_Vehicle_Population_Data.csv'
    print(f"Loading data from {FileName}")
    Data = ReadCleanData(FileName)

    while True:
        ShowMenu()
        choice = input("Enter your choice:")
        
        if choice == '1':
            ElectricRangeGraph(Data)
        elif choice == '2':
            MarketPie(Data)
        elif choice == '3':
            CityPie(Data)
        elif choice == '4':
            AgeRangeGraph(Data)
        elif choice == '5':
            ModelPie(Data)
        elif choice == '6':
            Averages(Data)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again")
