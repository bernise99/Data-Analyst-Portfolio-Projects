# Ordering data without sort or data structures.
print('\n###Data ordering###\n')

#Open files
file_one = open("File1.txt")
file_two = open("File2.txt")
file_three = open("File3.txt")
final_file = open("File4.txt", 'w')

number = ''
new_lst = []

# Read each line and eliminate the line break and then 
# create a single list to work on just one and not with three

for x in file_one:
    number = int(x)
    new_lst.append(number)
for y in file_two:
    number = int(y)
    new_lst.append(number)
for z in file_three:
    number = int(z)
    new_lst.append(number)

# Bubble sort

for i in range(len(new_lst)):
    for j in range(0, len(new_lst)-1-i):
        if new_lst[j] >new_lst[j+1]:
            aux =new_lst[j]
            new_lst[j] =new_lst[j+1]
            new_lst[j+1] = aux

print(new_lst)

#Write the sorted list in File4.txt
for num in new_lst:
    final_file.write(str(num)+'\n')

file_one.close()
file_two.close()
file_three.close()
