world_capitals = {
    "New Zealand":"Wellington",
    "Australia":"Canberra",
    "Australia":"Sydney"  
}

#adding values
world_capitals["India"]="New Delhi"
print(world_capitals)

for i in world_capitals:
    print(i)

for i in world_capitals.values():
    print(i)

#access values

print(world_capitals["New Zealand"])
world_capitals["Australia"] = "sydney"
print(world_capitals)

del world_capitals["Australia"]
print(world_capitals)

if "japan" in world_capitals:
    print("no error")
    
else:
    print("error")

print(len(world_capitals))