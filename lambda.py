# Lambda
#
#
# You are given code that should calculate the corresponding percentage tax of a price.


price = int(input())
tax_perc = int(input())

tax = (lambda x,y:(y*x)/100)(price, tax_perc)

print(tax)