
# Student Marks Analyzer

print("===== STUDENT MARKS ANALYZER =====")

# Accept student details
name = input("Enter student name: ")

# Accept number of subjects
n = int(input("Enter number of subjects: "))

subjects = []
marks = []

# Input subject names and marks
for i in range(n):
    subject = input(f"\nEnter subject {i+1} name: ")
    mark = float(input(f"Enter marks in {subject} (out of 100): "))

    if mark < 0 or mark > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        exit()

    subjects.append(subject)
    marks.append(mark)

# Calculate total, average and percentage
total = sum(marks)
average = total / n
percentage = (total / (n * 100)) * 100

# Assign grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

# Find highest and lowest marks
highest = max(marks)
lowest = min(marks)

high_index = marks.index(highest)
low_index = marks.index(lowest)

# Display result
print("\n========== STUDENT RESULT ==========")

print("Student Name:", name)
print("Total Marks:", total, "/", n * 100)
print("Average Marks:", round(average, 2))
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

print("\nHighest Marks:", highest, "-", subjects[high_index])
print("Lowest Marks:", lowest, "-", subjects[low_index])

print("===================================")
