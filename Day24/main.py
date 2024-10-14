with open("myFile.txt") as file:
    contents = file.read()
    print(contents)

with open("myFile.txt","a") as file:
    file.write("help me out again and again\n")


