frontend = {"ganga","abhiraj","mahadevan"}
Backend = {"anagha","amritha","abhi"}
Backend.add("akshay")
print(Backend)
frontend.remove("ganga")
print(frontend)

# Students enrolled in both courses
print(frontend & Backend)

# Students only in Backend
print(Backend - frontend)

# Total unique students
print(len(frontend | Backend))

# Create a dictionary
course = {
    "Frontend": len(frontend),
    "Backend": len(Backend)
}

# Print course names and student counts
for x, y in course.items():
    print(f"Course: {x}, Students: {y}")


# Dictionary comprehension to add Fullstack
new_course = {
    x: y for x, y in course.items()
}
new_course["Fullstack"] = sum(course.values())

print(new_course)

