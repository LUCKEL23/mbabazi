score = 50
submitted_project = True
if score >= 80 and submitted_project:

    print("A+")
elif score <=50: 
    print("A")
elif score>=95:
    print("b")
elif score == 50:
    print("passed")
else:
    print("f")

age = 70
size = 6
print("a" if age >=70 else "fali" if size <10 else "m")
     
    # elifs multiple condit
#match case
country = ("uganda")
match country:
    case "united states":
        print("us")
    case "india":
        print ("IN")
    case "uganda":
        print("ug")

email = " luc@ky@c.omthj "
email = email.strip()
if email =="":
    print("email cant be emptu")
elif not ( '.' in email and '@' in email):
    print("email must contain . and @")
elif email.count('@')!=1:
    print("email must contain one @")
elif not email.endswith('com'):
    print("must end")


else:
    print(" email is valid")



    
        
        

