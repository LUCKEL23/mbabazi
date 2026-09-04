#basic loop
"""
syntax -
for condition:
    body
    else:
        executes after the loop has ended| clean up logic
        """
for x in range(10):
    print(x+1, end="")
    # conditions
for x in range(10):
    # only select even numbers during the interation
    if x % 2==0:
        print(x)
#loop that will only display names
names = ["dave","mercy","daniella","sharon"]
names_count = len(names)
for name in names:
    if len(name)<=5:print(name)

#break and continue statements
for x in range(11):
    if x in (3,7,9):
        continue
    print(x)
#while loop
count = 0
while count < 10:
    if count in [4,6]:
        count += 1# very important to avoid  infinite
        continue
    print(count)
    count += 1

count = 0
# while true
while True:
    print(count)
    if count ==5:
        break
    count += 1
# python user enter a work.

while True:
    work = input("enter work : word or character") 
      
    if work in ["q","quit"]:
        break
    print(f"you entered {work}")
    # 
    
    