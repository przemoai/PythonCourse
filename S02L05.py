import math
import time
formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range (1000000):
    argument_list.append(i/10)

for formula in formulas_list:
    results_list=[]
    print("We are working with {}".format(formula))
    start=time.time()
    for x in argument_list:
        results_list.append(eval(formula))

    print("Max value: {} \nMin value {}".format(max(results_list),min(results_list)))

    stop=time.time()

    print("Operation last: {}".format(stop-start))

print(30*"--")
for formula in formulas_list:
    results_list=[]
    print("We are working with {}".format(formula))
    start=time.time()
    compiled_formula = compile(formula,formula,'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))

    print("Max value: {} \nMin value {}".format(max(results_list),min(results_list)))

    stop=time.time()

    print("Operation last: {}".format(stop-start))