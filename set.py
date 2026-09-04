fruits = {"apples" , "berries" , "banana" , "lemons"}
print(len(fruits))
fruits.add("passion")
print(fruits)
others = {"pawpaw", "melon"}
fruits.update(others)
print(fruits)
fruits.remove("banana")#
print(fruits)
fruits.discard("lemons")
print(fruits)
random = fruits.pop()
print(random)
x = {2,4,6,8,10}
y = {1,3,5,2,8}
common = x.intersection(y)
print(common)
difference = x.difference(y)
print(difference)
x.intersection_update(y)#modifies the original set
print(x)
#check set,super,intercestion
print(x.isdisjoint(y))
copy = x.copy()
print(copy)
cities = ["mbale","gulu" , "mbale", "mbarara","kampala"]
print(cities)
no_duplicate = []
for city in cities:
    if city not in no_duplicate:
        no_duplicate.append(city)
print(no_duplicate)



