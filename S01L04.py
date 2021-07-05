import os

def readFile(path):
    with open(path,'r') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count





path = r'C:\Users\przemoai\Desktop\PythonKurs\S001L004\file.txt'

# if os.path.isfile(path):
#     print("There are {} words in file {}".format(readFile(path),path))
# else:
#     print("file doesnt exist")


os.path.isfile(path) and print("There are {} words in file {}".format(readFile(path),path))