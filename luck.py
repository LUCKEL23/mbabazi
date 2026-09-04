def greet(name, greeting='hello'):
     message = f"{greeting}, {name}"
     return message
result = greet("alice")
print(result)
def add(a,b):
    result = a + b
    return result
total = add(4,7)
print(total)
def nums(*args):
    result = [p + 2 for p in args]
    return result
print(nums(1,2,3,4))
print(max(4,3))
def greet(name):
    return f"hi!, {name}"
print(greet("lucky"))
say_hello = greet
print(say_hello("alice"))

def animal_type(animal,name):
    return f"i have pet {animal} named {name}"
print(animal_type("dog","muga"))

def profile(name,age,school):
    return f"am {name} , {age} years from {school}"
print(profile("lucky","21","masam"))
def sum_all(*args):
    total = 0
    for n in args:
          total += n
    return total

print(sum_all(1,2,3,4))

#kwargs are assined to specific value with =

def profile(**kwargs):
    print(f"my name {kwargs['name']} from  {kwargs['country']} , age of {kwargs ['age']}, and i love {['hobby']}")

profile(name= "lucky" , country= "uga", age = "21" , hobby  = "swim")



 