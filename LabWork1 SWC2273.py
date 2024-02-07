"""
    Program Purpose: To Create Python program to convert an amount in Malaysian Ringgit (MYR) to a selected target currencies
    Programmer: Muhammad Muqry Bin Razaly
    Date 7 February 2024
"""
print("Currency Conversion Program")
print("")

print("Exchange Rates:")
print("USD - US Dollar: 0.21")
print("EUR - Euro: 0.20")
print("SGD - Singapore Dollar: 0.28")
print("")

#user need to choose currency to convert (1 USD, 2 EURO, 3 SGD)
print("please choose the target currency:")
a = print("1. USD - US Dollar")
b = print("2. EUR - Euro")
c = print("3. SGD - Singapore Dollar")

#if user choose 1 (USD - US Dollar) then:
choose = input("\nPlease choose (1-3):")
if choose == '1':
    USD = float(input ("Enter the amount in Malaysia Ringgit (MYR) :")) #
    USD_formula= USD * 0.21 #
    print("Equivalent amount in USD - US Dollar is: %.2f" % USD_formula)

#if user choose 2 (EUR - Euro) then:
elif choose == '2':
    EUR = float(input ("Enter the amount in Malaysia Ringgit (MYR) :")) #
    EUR_formula= EUR * 0.20 #
    print("Equivalent amount in EUR - Euro is: %.2f" % EUR_formula)

#if user choose 3 (SGD - Singapore Dollar) then:
elif choose == '3':
    SGD = float(input ("Enter the amount in Malaysia Ringgit (MYR) :")) #
    SGD_formula= SGD * 0.28 #
    print("Equivalent amount in SGD - Singapore Dollar is: %.2f" % SGD_formula)

#if user enter besides 1,2 or 3 then:
else:
    print("INVALID OPTION!!!, please reenter number (1 or 2 or 3)")