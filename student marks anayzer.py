import csv
import os


# 1. VALIDATE MARKS
def validate_mark(mark):
    """
    Check whether marks are between 0 and 100.
    """
    return 0 <= mark <= 100


# 2. INPUT STUDENT NAME
def input_student_name():
    """
    Take student name from the user.
    """

    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name

        print("Student name cannot be empty.")


# 3. INPUT SUBJECTS AND MARKS
def input_marks():
    subjects = []
    marks = []

    while True:
        try:
            number_of_subjects = int(
                input("Enter number of subjects: ")
            )

            if number_of_subjects <= 0:
                print(
                    "Invalid input! "
                    "Number of subjects must be greater than 0."
                )
            else:
                break

        except ValueError:
            print(
                "Invalid input! "
                "Please enter a valid whole number."
            )

    for i in range(number_of_subjects):

        # Input subject name
        while True:
            subject = input(
                f"\nEnter subject {i + 1} name: "
            ).strip()

            if subject:
                break

            print("Subject name cannot be empty.")

        # Input marks
        while True:
            try:
                mark = float(
                    input(
                        f"Enter marks in {subject} "
                        "(out of 100): "
                    )
                )

                if not validate_mark(mark):
                    print(
                        "Invalid marks! "
                        "Enter marks between 0 and 100."
                    )
                    continue

                break

            except ValueError:
                print(
                    "Invalid input! "
                    "Please enter a numeric value."
                )

        subjects.append(subject)
        marks.append(mark)

    return subjects, marks


# 4. CALCULATE TOTAL
def calculate_total(marks):
    """
    Calculate total marks.
    """
    return sum(marks)


# 5. CALCULATE AVERAGE
def calculate_average(marks):
    """
    Calculate average marks.
    """

    if not marks:
        return 0

    return calculate_total(marks) / len(marks)


# 6. CALCULATE PERCENTAGE
def calculate_percentage(marks):
    """
    Calculate percentage.
    """

    if not marks:
        return 0

    total = calculate_total(marks)
    maximum_marks = len(marks) * 100

    return (total / maximum_marks) * 100


# 7. ASSIGN GRADE
def assign_grade(percentage):
    """
    Assign grade according to percentage.
    """

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    elif percentage >= 40:
        return "E"

    else:
        return "F"


# 8. FIND HIGHEST MARKS
def find_highest(marks):
    """
    Find the highest marks.
    """
    return max(marks)


# 9. FIND LOWEST MARKS
def find_lowest(marks):
    """
    Find the lowest marks.
    """
    return min(marks)


# 10. DISPLAY STUDENT REPORT
def display_report(name, subjects, marks):
    """
    Calculate and display the complete student report.
    """

    total = calculate_total(marks)
    average = calculate_average(marks)
    percentage = calculate_percentage(marks)
    grade = assign_grade(percentage)

    highest = find_highest(marks)
    lowest = find_lowest(marks)

    highest_index = marks.index(highest)
    lowest_index = marks.index(lowest)

    print("\n")
    print("========================================")
    print("          STUDENT RESULT")
    print("========================================")

    print("Student Name :", name)

    print(
        "Total Marks  :",
        total,
        "/",
        len(marks) * 100
    )

    print(
        "Average Marks:",
        round(average, 2)
    )

    print(
        "Percentage   :",
        round(percentage, 2),
        "%"
    )

    print("Grade        :", grade)

    print("----------------------------------------")

    print(
        "Highest Marks:",
        highest,
        "-",
        subjects[highest_index]
    )

    print(
        "Lowest Marks :",
        lowest,
        "-",
        subjects[lowest_index]
    )

    print("========================================")

    return total, average, percentage, grade


# 11. SAVE RESULT TO CSV
def save_to_csv(
    name,
    subjects,
    marks,
    total,
    average,
    percentage,
    grade
):
    """
    Save student's result to results.csv
    in the Student Marks Analyzer folder.
    """

    # Exact folder where CSV will be saved
    folder_path = r"C:\Users\Bhanvi\Desktop\Ayushi projects\student-marks-analyzer"

    # Create folder if it does not already exist
    os.makedirs(folder_path, exist_ok=True)

    # Complete path of CSV file
    filename = os.path.join(folder_path, "results.csv")

    # Check whether CSV file already exists
    file_exists = os.path.exists(filename)

    # Open CSV file in append mode
    with open(
        filename,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        # Add header only when file is new
        if not file_exists:
            writer.writerow([
                "Student Name",
                "Subject",
                "Marks",
                "Total Marks",
                "Average",
                "Percentage",
                "Grade"
            ])

        # Save each subject result
        for subject, mark in zip(subjects, marks):
            writer.writerow([
                name,
                subject,
                mark,
                round(total, 2),
                round(average, 2),
                round(percentage, 2),
                grade
            ])

    print("\nResult saved successfully!")
    print("CSV file location:")
    print(filename)


# 12. MAIN PROGRAM
def main():

    name = input_student_name()

    subjects, marks = input_marks()

    total, average, percentage, grade = display_report(
        name,
        subjects,
        marks
    )

    save_to_csv(
        name,
        subjects,
        marks,
        total,
        average,
        percentage,
        grade
    )


# RUN THE PROGRAM
if __name__ == "__main__":
    main()a
