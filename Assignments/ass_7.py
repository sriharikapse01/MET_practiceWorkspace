students = {
   "Alice": (85, 90, 78),
   "Bob": (50, 45, 60)
}
name = input("Enter a student name :")

if name in students:
    marks = students[name]
    avg = sum(marks) / len(marks)
    if avg >= 60:
        print("passed")
    else:
        print("failed")
        
else:
    print("Student not found")