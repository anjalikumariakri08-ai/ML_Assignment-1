import pandas as pd
data = {
    "Student Name": ["Anjali", "Rahul", "Priya", "Aman", "Sneha"],
    "Roll Number": [101, 102, 103, 104, 105],
    "Marks": [95, 85, 72, 65, 88]
}
df = pd.DataFrame(data)
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
df["Grade"] = df["Marks"].apply(calculate_grade)
print(df)
