###############
# Implementation of Stock Profit Calculator
#
##############

# Declare variables with default values

tickerSymbol = 'ADBE'
allotment = 100
finalSharePrice = 110
sellCommission = 15
initialSharePrice = 25
buyCommission = 10
capitalGainTaxRate = 15 # in percent

# Get inputs from console

tickerSymbol = input("Enter the Stock Symbol")
allotment = int(input("Enter number of shares allotted"))

initialSharePrice = int(input("Enter starting share price($)"))
buyCommission = int(input("Enter total buying commission($)"))

finalSharePrice = int(input("Enter selling share price($)"))
sellCommission = int(input("Enter total selling commission($)"))

capitalGainTaxRate = int(input("Enter captial gain tax rate(%)"))

# define a function to calculate stock profit calculator

def stockProfitCalc() :
  
  # calculate initial and final price
  
    finalPrice = (allotment * finalSharePrice) - sellCommission
    initalPrice = (allotment * initialSharePrice) + buyCommission
    
    # calculate profit
    
    profit = finalPrice - initalPrice
    
    # caluclate tax
    
    tax = (capitalGainTaxRate / 100) * profit
    
    # calculate final netprofit and cost
    
    netProfit = profit - tax
    cost = (finalSharePrice * allotment) - netProfit
    
    # get ROI 
    
    roi = ( ( (netProfit - cost) / cost ) * 100 ) + 100 # converting to percentage
    
    # calculate break even
    
    breakeven = initialSharePrice+( buyCommission + sellCommission  )/100
    
    # Print the following information
    
    print(" PROFIT REPORT for : "+tickerSymbol)
    print(" Proceeds : "+str(finalSharePrice*allotment)+"$")
    print(" Cost : $"+str(cost))
    print(" Cost Details : \n")
    print(" Total Purchase Price : "+str(allotment * initialSharePrice))
    print(" Buy Commission : $"+str(buyCommission))
    print(" Sell Commission : $"+str(sellCommission))
    print(" Tax on Capital Gain = "+str(capitalGainTaxRate)+"% of $"+str(profit)+"\n")
    print(" Net Profit : $"+str(netProfit))
    print(" ROI :"+str(roi)+"%")
    print(" To break even, you should have a final share price of $"+str(breakeven))

stockProfitCalc();
