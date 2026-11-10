python = {"ganga","abhiraj","mahadevan"}
DataScience = {"anagha","amritha","abhi"}
python.add("akshay")
print(python)
DataScience.remove("abhi")
print(DataScience)
print(python & DataScience)
print(python - DataScience)
print(python | DataScience)
course = {
    "Python" : len(python) ,
    "DataScience" : len(DataScience)
}

for x, y in course.items():
  print(x, y)


squares = {x: y*2 for x,y in course.items()}
print(squares)