student_marks = {'Krishna': 68.0, 'Arjun': 77.0, 'Malika': 56.0}
query_name = 'Malika'

if query_name in student_marks:
    matchedScore = student_marks[query_name]
    # print(matchedScore)
    print(f"{matchedScore:.2f}")