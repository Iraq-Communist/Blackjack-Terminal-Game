import random 


File = open("Word_list.txt")
lines = File.readlines() 

Random_Word = random. randint(1,2317)
print(lines[Random_Word])