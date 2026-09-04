#grading
user = int(input("enter the number"))
if user >=90:
    print("excellent")
elif user >=80:
    print("good")
elif user <=70:
    print("fair")
elif user >=60:
    print("d")
else:
    print("try again")

    day = 2
    match day:
        case 1:
            print("monday")
        case 2:
            print("tuesday")
#list
names = ["lucky" ,"hope", "jackie"]
print(names[2])#jackie

names.append("mug")
print(names)#adds mug to the list
other_names = ("joke" ,"mathew")
names.extend(other_names)
#deletion
names.remove("hope")
names.extend(["lucky","joke", "mug"])
print(names)
#list of complehensins
names_upper = [name.upper() for name in names]
print(names_upper)
# list with length
length = [len(name) for name in names]
print(length)
above =[name.title  for name in names if len(name) > 5]
print(above)
true_even = [True if len(name)%2==0 else false for name in names ]




    

