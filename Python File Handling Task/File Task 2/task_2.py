#write mode
fileName = open("task2.txt","w")
list = ["India \n","Gujarat \n","Ahmedabd \n"]

fileName.writelines(list)
fileName.close()

#Append Mode
fileName = open("task2.txt","a")

fileName.write("\n")
fileName.write("Hello World from Ahmedabad \n")

fileName.write("Hello India")

#read mode
fileName = open("task2.txt","r")
print("### Append in file  ###")

print(fileName.read())
print()

fileName.close()