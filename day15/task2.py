class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print(f"Student: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    def check_result(self):
        if self.marks > 40:
            print("Status: ✅ Passed")
        else:
            print("Status: ❌ Failed")
s1 = Student("Riya Sharma", 21, 85)

s1.display_info()
s1.check_result()
