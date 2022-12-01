d ={}
entryIndex = 0
currentElfValue = 0

with open("C:\\Users\imcnamara\Desktop\Puzzle1Input.txt", "r") as file:
   for line in file:
       if line.strip() == "":
           entryIndex += 1
           currentElfValue = 0
       else:
           currentElfValue += int(line.strip())
           d["Elf"+str(entryIndex)] = currentElfValue
           
answer1 = max(d, key=d.get)
print('Answer 1 is', d[answer1])

sortedKeys = sorted(d, key=d.get, reverse=True)[:3]

answer2 = d[sortedKeys[0]] + d[sortedKeys[1]] + d[sortedKeys[2]]
print('Answer 2 is', answer2)
           
