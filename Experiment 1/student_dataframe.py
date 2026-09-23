import pandas as pd
data = {
    "Student Name": ["Anjali", "Rahul", "Priya", "Aman", "Sneha"],
    "Roll Number": [101, 102, 103, 104, 105],
    "Marks": [85, 76, 92, 68, 88],
    "Attendance": [90, 85, 95, 80, 92]
}
df = pd.DataFrame(data)
result = df[df["Marks"] > 80]
print("Students who scored above 80 marks:")
print(result)
