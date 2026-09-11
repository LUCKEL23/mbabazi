text = "HELLO @yVu students.Welcome to 2026!"

upper = sum( 1 for c in text if c.isupper())
print(upper)
lower = sum(1 for c in text if c.islower())
print(lower)
digit = sum(1 for c in text if c.isdigit())
print("digits",digit)
print(text.count(" "))
print(text.replace("2026","2024"))
print(len(text))



