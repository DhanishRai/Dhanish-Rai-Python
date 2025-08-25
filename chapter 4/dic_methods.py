marks={
    "harry":100,#here harry is key and 100 is value
    "shubham":56,
    "rohan":34,
    "list":[1,3]
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry":99})
print(marks )
# IMPORTANT FOR INTERVIEWS 
print(marks.get("harry"))
print(marks["harry"])
print(marks.get("harry2"))#prints None if key value is not present
print(marks["harry2"])#prints error if key value is not present

 