
def gen_letter_grade(score:float) -> str:
    if not (0 <= score <=100):
        raise ValueError(f"Score must be between 0 and 100, got {score}")
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def grade_remark(grade:str) -> str:
    remarks = {
        'A': "Excellent work!",
        'B': "Good job!",
        'C': "Fair effort.",
        'D': "Needs improvement.",
        'F': "Failing grade."
    }
    return remarks.get(grade, "Invalid grade")

def evaluation(name: str , score:float) -> str:
    grade = gen_letter_grade(score)
    remark = grade_remark(grade)
    status = "PASS" if grade !='F' else "FAIL"
    return f"{name} scored {score}, which is a grade of {grade}. {remark} and has a status of {status}."

if __name__ == "__main__":
    student : list[tuple[str,float]] = [("Alice", 95), ("Bob", 82), ("Charlie", 67), ("David", 58), ("Eve", 73),("robb", 173)]
    for name, score in student:
        print(evaluation(name, score))






