import os


files_to_process = [
    r"C:\Users\AGAiN\Desktop\PythonKurs\S002\skrypt1.py",
    r"C:\Users\AGAiN\Desktop\PythonKurs\S002\skrypt2.py"
    ]

for file_path in files_to_process:
    with open(file_path,'r') as f:
        print("File {}".format(os.path.basename(file_path)))
        source = f.read()
        exec(source)

