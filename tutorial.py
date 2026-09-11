word = print("your laerning:\n\t- python basics\n\t-data stractures\n\t-ai ")
print(""" i love python\t
 basic\t 
 ai tools""")
name = "lucky"
print("my name is", name)
print(name,"loves python")
print(name.upper())
num = 40
print(num.bit_length())
print("that is num"+ str(num))
text = """python is good
python is simple
python is easy"""
print(text.count("python"))
print(text.count(" "))
date = "23/45/67.56"
print(date.replace("/","-"))
#to remove u just use space 
print(date.replace("/",""))
print(date.replace("/","-").replace(".",","))
numb = "+49 (176) 123-4567"
print(numb.replace("+","").replace("(","").replace("-","").replace(")",""))
#trasformation
first = " mbabazi " .strip()
last = "racheal"
age = 40
combine = first + " " + last
print(combine)
print("my first is "+ first + ",and " + last + "and age is "  + str(age)+ "")
print("=="*10)
print(first[1:])
print(first[-2:])
print(first)
search = "EMAIL".lower()
DATA = "email".lower()
print(search == DATA)
infor = "986-maria, (data engineer) ;; 27yrs..".strip()
print(infor.startswith("986"))
print("8" in infor)
print(infor.find("maria"))
print(infor. isalpha())
print(infor.split())

