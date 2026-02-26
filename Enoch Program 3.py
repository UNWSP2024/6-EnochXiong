def calculateTax(sales, rate):
    tax = sales * rate
    return tax

totalSales = float(input("Enter total sales for the month: "))

STATE_RATE = 0.05
COUNTY_RATE = .25

stateTax = calculateTax(totalSales, STATE_RATE)
countyTax = calculateTax(totalSales, COUNTY_RATE)

totalTax = stateTax + countyTax

print("State sales tax: $", round(stateTax))
print("County sales tax: $", round(countyTax))
print("Total sales tax: $", round(totalTax))
