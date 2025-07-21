grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
print("Grade Tracker")
print("Students:", grades)
avg = sum(grades.values()) / len(grades)
print("Average grade:", avg)
high=max(grades, key=grades.get)
low = min(grades, key=grades.get)
print("Highest scorer:", high, "(", grades[high], ")")
print("Lowest scorer:", low, "(", grades[low], ")")
grades['David']=88
print("After adding David:", grades)
grades['Alice']=90
print("After updating Alice:", grades)
