def calculate_paint(efficency_ltr_per_m2,*args):
    amount=sum(args)




    return amount*efficency_ltr_per_m2


print(calculate_paint(0.2,5,6,7,8))

rooms=[5,6,7,8]

print(calculate_paint(0.2,*rooms))