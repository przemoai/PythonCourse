

def DisplayOptions(options):
    for i in range(len(options)):
        print(i,' - ',options[i],'\n')

    choice = input("Select option above or press enter to exit: \n")
    return choice


options = ['load data','export data','analyze & predict']
choice = 'x'

while choice:
    choice = DisplayOptions(options)

    if choice:
        try:
            choice_num = int(choice)-1

            if choice_num >=0 and choice_num<len(options):
                print("Selected {} - {}".format(choice_num+1,options[choice_num]))
            else:
                print("Num out of list")
        except:
            print("You need to enter value")
    else:
        print("--END--")