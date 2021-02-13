file = open("task5Notes.txt","r")

count = 0 

for line in file:
    words = line.split()

    for word in words:
        count += 1

print("Words Count :: {}".format(count))