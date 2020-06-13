from TicTacToe import *
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import random
import seaborn as sns
from fbprophet import Prophet

#Taking input from user 
print("What would you like to do? \n1. Look into Avocado prediction\n2. Play a Tic Tac Toe game \n ")
option = int(input())

# Logic for TicTacToe game
if( option == 2):
    Draw_Board() #Draws board
    while True:
        Player_1()  #Player 1's turn
        Draw_Board()
        if Winner_Check('X')==True:  #Checks if Player 1 is winner and specifies the steps to perform
            print("Player #1 Wins")
            break;
        if Winner_Check('X')==False:    
            break;

        Player_2()  #Player 2's turn
        Draw_Board()
        if Winner_Check('O')==True:     #Checks if Player 2 is winner and specifies the steps to perform
            print("Player #2 Wins")
            break;
        if Winner_Check('O')==False:
            break;

if(option == 1):

    ##IMPORTING DATA
    
    avocado_df = pd.read_csv('avocado.csv')

    ##EXPLORING DATASET
    
    # Let's view the head of the dataset
    print(avocado_df.head())
    
    # Let's view the last 5 elements in dataset
    print(avocado_df.tail(5))

    #Sorting Data by Date
    print("Sorting data by Date")
    avocado_df = avocado_df.sort_values("Date")

    #Plot for showing the distribution of Price
    print("Plot for showing the distribution of Price")
    plt.title("Distplot for AveragePrice")
    ax = sns.distplot(avocado_df["AveragePrice"], color = 'y')
    plt.show()

    #Plot to show average price by date
    plt.title("Price by Date")
    datePriceGroup = avocado_df.groupby('Date').mean()
    datePriceGroup['AveragePrice'].plot(x=avocado_df.Date, color='green')
    plt.show()

    #Plot to show types of avocado
    print("Plot to show types of avocado")
    plt.title("Types of Avocado by AveragePrice")
    sns.boxplot(x="type", y="AveragePrice", data=avocado_df, palette = 'pastel')
    plt.show()

    #Correlation Matrix
    plt.title("Correlation matrix of 4 attributes of dataset")
    cordf = pd.DataFrame(avocado_df,columns=['AveragePrice','year','Total Volume', 'Total Bags'])
    corrMatrix = cordf.corr()
    sns.heatmap(corrMatrix, annot = True,square = True)
    plt.show()

    
    ##FORCASTING
    
    avocado_prediction_df = avocado_df[['Date', 'AveragePrice']]
    avocado_prediction_df = avocado_prediction_df.rename(columns={'Date':'ds', 'AveragePrice':'y'})
    print(avocado_prediction_df)


    m = Prophet()
    m.fit(avocado_prediction_df)

    future = m.make_future_dataframe(periods=365)
    forecast = m.predict(future)

    print(forecast)

    forecastdf = pd.DataFrame(forecast)
    forecastdf.to_excel("output.xlsx")

