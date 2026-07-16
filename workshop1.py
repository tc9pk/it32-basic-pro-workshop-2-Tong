quantity = input("Enter the quantity: ")
cost_price = input("Enter the cost price: ")
sell_price = input("Enter the selling price: ")
team_member = input("Enter the team member's name: ")

cost = int(quantity) * float(cost_price)
print(cost)
sell = int(quantity) * float(sell_price)
print(sell)
profit = sell - cost
print(profit)
per = profit * (20/100)
print(per)
teamcost = (profit - per) / int(team_member)
print(teamcost)
tong
