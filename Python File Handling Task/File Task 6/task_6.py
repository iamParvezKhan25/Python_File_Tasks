file  = ("task6Notes.txt","r")
count = 0

for line in file:
    words = line.split()

    for i in words:
        if i == "the" or i == "The":
            count += 1
    print(count)
        
    
print(count)