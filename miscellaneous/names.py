


file = open(r'C:\WiseOwl\miscellaneous\names.txt','r')

count = 0 

for line in file:
    #if line.strip() != "":
    if line.strip() == "Alice":
        count = count + 1

file.close()

print("Non-empty lines:", count)  



