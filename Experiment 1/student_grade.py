import pandas as pd

# Create DataFrame
data = {
    "Student Name": ["Anjali", "Rahul", "Priya", "Aman", "Sneha"],
    "Roll Number": [101, 102, 103, 104, 105],
    "Marks": [95, 85, 72, 65, 88]
}

df = pd.DataFrame(data)

# Dynamically calculate Grade based on Marks
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

# Add Grade column
df["Grade"] = df["Marks"].apply(calculate_grade)

# Display DataFrame
print(df)