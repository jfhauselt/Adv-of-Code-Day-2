path = r"C:\Users\jfhau\Documents\#code\Day2.txt"
#creating a list that constains list
entries =[]
# each sub list will have things at indexes
#index 0 min password count
#index 1 max password count 
#index 2 the character
#index 3 the password
def showResults(valid,invalid):
    print("Valid: " +str(valid))
    print("Invalid: "+ str(invalid))

for line in open(path,"r"):
    product = []
    entry = line.split()
    product.append(int(entry[0].split("-")[0]))
    product.append(int(entry[0].split("-")[1]))
    product.append(entry[1][0])
    product.append(entry[2])
    entries.append(product)

valid = 0 
invalid = 0
for entry in entries:
    count = 0
    for char in entry[3]:
        if char is entry[2]:
            count +=1
    if count >= entry[0] and count <= entry[1]:
        valid +=1
    else:
        invalid += 1

showResults(valid,invalid)

#Part 2
valid = 0 
invalid = 0
for entry in entries:
    if len(entry[3]) < entry[1]:
        invalid +=1
    elif (entry[3][entry[0] -1] == entry[2]) != (entry[3][entry[1] -1] == entry[2]):
        valid +=1
    else:
        invalid += 1

showResults(valid,invalid)
