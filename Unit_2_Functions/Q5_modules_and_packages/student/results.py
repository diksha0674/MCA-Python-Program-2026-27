def show_result(obtained_marks, total_marks):
    percentage = (obtained_marks / total_marks) * 100 if total_marks else 0
    print("\nStudent Result")
    print("Obtained Marks:", obtained_marks)
    print("Total Marks:", total_marks)
    print("Percentage:", round(percentage, 2), "%")
