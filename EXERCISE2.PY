marks = {"john": 78,"mary": 92 ,"peter": 65, "sarah": "85" , "david": "55"}
# display all students with there marks
for key , value in marks.items():
    print(f"{key},  {value}")
parent = input("Enter your childs name to see there marks")
if parent == "john":#corrections
    print("78")#if parent in marks: marks[parent] else print("invalid stdnt".center(20,"*"))
elif parent == "mary":
    print("98")
elif parent =="peter":
    print("65")
elif parent == "sarah":
    print("85")
elif parent == "david":
    print("55")
else:
    print("student not found")

marks["mbabazi"] = 90
marks["david"] = 88
del marks["mary"]
sorted_dict = dict(sorted(marks.items(), key=lambda item:item[1]))
#student with the highest mark
highest = max(marks,key=marks.get)
print(f"highest {highest} is {marks.[highest]}")