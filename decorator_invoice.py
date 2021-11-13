# You are working on an invoicing system.
# The system has an already defined invoice() function, which takes the invoice number as argument and outputs it.
# You need to add a decorator for the invoice() function, that will print the invoice in the following format:
# Sample Input
# 42
#
# Sample Output
# ***
# INVOICE #42
# ***
# END OF PAGE

def decor(fun):
    def wrap(num):
        print("***")
        fun(num)
        print("***")
        print("END OF THE PAGE")
    return wrap

@decor
def invoice(num):
    print("INVOICE #" +num)

invoice(input());

