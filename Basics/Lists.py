
#* Declaration 
marks=[2,6,7,8,9]  #Lists are in square brackets & marks[5] yeh nhi likhte
print(marks[0])
for i in range(5):
    print(marks[i],end = " ")  # bina newline mei gye hue exechute krna sikhe

#*python mei piche se bhi indexing kr skte hai
print(marks[-1])
print(marks[-2])
print(marks[-3])

# Outout
# 9
# 8
# 7

#*Python mei loop ki zarurat hi nhi hai list ko print krne ke liye
print(marks[0:3],end = " ")

#*Implementation of for loop in lists
for i in marks:
    print(i,end = " ")

#*Using .append() function to enter an element in the List

marks.append(2)
print(marks)

#*Using .insert() function to enter an element in the List 

print("Marks Before : ",marks)
marks.insert(0,4)
print("Marks After : ",marks)

#*Using (in)
print("Check whether there is 2 in the Lists : ",2 in marks)
# Output
# True

#*Taking length of a List using len()
print("Length of the List is : ",len(marks))
i = 0
while i < len(marks) : 
    print(marks[i],end =" ")
    i+=1

#*Using .clear() to empty the List

print("List Before : ",marks)
marks.clear()
print("List Now : ",marks)

#*Use break;/continue; statement  //for example : 
Students =["Milind","Aman","Sourish","Rajneesh"]
for i in Students:
    if i == "Aman":
        print("Yeh toh Gandu hai")
        break;
    else: 
        continue;
