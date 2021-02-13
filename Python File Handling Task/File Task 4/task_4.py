file = open("task4Story.txt","r")
count = 0

for line in file:
    if line[0] not in 'T':
        count += 1

file.close()
print("Not Start With T : {}".format(count))