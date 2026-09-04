#DICTIONARIES
info = {"NAME": "lucky", "Nationality":"ugandan", "age":"20"}
print(info["NAME" ])
info["size"] = 30#adds a new key to the list of imfo
del info["age"]
print("info")
sorted_dict = dict(sorted(info.items(1)))#default sortng is on the keys\ascendind
for key,value in info.items():
    print(key,value)
    info.pop("NAME")


