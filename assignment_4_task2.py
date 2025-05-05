try:
    f = open("output.txt", "x")
    f.close()
except FileExistsError:
    print("File exists. Proceeding with existing file.")


with open("output.txt","w") as f:
    x= input("Enter text to write to the file:")
    f.write(x)
    print("data successfully written to output.txt.")

with open("output.txt","a") as f:
    x= input("Enter additional text to append:")
    f.write("\n" + x)
    print("data successfully appended.")

with open("output.txt","r") as f:
    print("Final content of output.txt:")
    print(f.read())