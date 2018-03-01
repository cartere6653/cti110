#CTI-110
#P2HW2-Tip Tax Total
#Eric Carter
#27Feb2018
#


#Constant of tip,& tax
TIP_RATE = 0.18
TAX_RATE = 0.07

#Varible of tip,tax,&total
tip = 0.00
tax = 0.00
total = 0.00

#calculate foodcost

foodcost = float( input("enter food cost:"))

#calculate tip 

tip = TIP_RATE * foodcost

#calculate tax

tax = TAX_RATE * foodcost

total = foodcost + tip + tax

print("food cost: $" + format(foodcost, ".2f"),"tip: $" +\
      format(tip,".2f"),"tax: $" + format(tax,".2f"),\
      "total: $" + format(total,".2f"),sep= "\n")
