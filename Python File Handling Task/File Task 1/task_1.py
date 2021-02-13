fileName = open("C:/Users/Khan/Desktop/Python File Handling Task/task1.txt")

numberOfLines = int(input("Enter Number of Lines ::"))

for i in range(numberOfLines):
    line = fileName.readline()
    print(line)