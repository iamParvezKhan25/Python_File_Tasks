file = open("C:/Users/Khan/Desktop/Python File Handling Task/File Task 8/task8Article.txt","r")

count = 0

for line in file:
    words = line.split()

    for word in words:
        if word =="this" or word == "these":
            count += 1
print(count)