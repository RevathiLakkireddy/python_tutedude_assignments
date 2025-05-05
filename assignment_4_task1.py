

#checking if the file exists and read all the content of the file
import os
if os.path.exists("sample_text_file"):
    with open("sample_text_file", "r") as x:
        print(x.read())

else:
    print("The file doesn't exists.")


#handiling file not found error if the file doesn't exist
try:
    with open("sample_text_file1", "r") as text1:
        print(text1.read())

except FileNotFoundError:
    print("file does not exists.")

