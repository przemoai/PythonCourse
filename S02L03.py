import math

argument_list = []

for x in range(101):
    argument_list.append(x/10)

formula = input("Input your function: ")

for x in argument_list:
    print("{0:3.1f} {1:6.2f}".format(x,eval(formula)))
