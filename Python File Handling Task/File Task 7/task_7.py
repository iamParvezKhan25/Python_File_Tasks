file = open("C:/Users/Khan/Desktop/Python File Handling Task/File Task 7/task7Poem.txt","r")

for line in file:
    words = line.split()

    for word in words:
        if len(word) < 4:
            print("Word :",word)