a = "this is a Book"

# INSERTS SPACE AT THE END OF THE EACH CHARACTER
for i in a :
    print(i,end=" ")

print()

#REVERSE THE STRING
for i in a[: : -1] :
    print(i,end=" ")

print()
print()
for i in a[-9:-2] :
    print(i,end=" ")

# print((a,end=" "*3))

print()

# CHECKS THE CHARACTER IS PRESENT IN THE STRING
print('a' in a)
print()
print('m' in a)


print()
#Comparison of String
c = 10
d ="10"
print(c==d)


print()
if a<d :
    print("a is less than c",len(a),len(c))
else :
    print("a is greater than c")


print()

#Remove the extra space
e = "moin "
print(e.strip())



#Remove the extra space in between
print()
f = "m o i n"
print(f)
print(f.replace(" ",""))

print()
#find
print(type(a.find("Book",10,15)))
print(a.find("Book",10,15))

print()

# h = input("Enter SubString : ")
# # print(a.find(h,10,15))


#returns true if string ends with substr
print()
print(a.endswith("Book"))

#capitalize first character

print(a.capitalize())
print()

#count the existence of a character
print(a.count("i"))

