def display_student_details(*subjects, **details):
    print("Enrolled Subjects:")
    for sub in subjects:
        print(f"- {sub}")
        
    print("\nStudent Info:")
    for key, value in details.items():
        print(f"{key}: {value}")

# Testing the function
display_student_details("Math", "Physics", "Python", name="Aman", age=21, grade="A")
