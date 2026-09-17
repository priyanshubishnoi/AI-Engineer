"""return stats for a list of scores"""
from collections import namedtuple


def processed_scores(scores:list[int])-> dict[str, int|float|list[int]]:
    unique_sorted  = sorted(set(scores))
    count = len(scores)
    return {"og":scores,
            "unique":unique_sorted,
            "count":count,
            "min":min(scores),
            "max":max(scores),
            "avg":sum(scores)/count
            }

"""Use set operations to analyse skill overlap between two teams."""
def skill_analysis(team_a: list[str],team_b: list[str])-> dict[str,set]:
    set_a = set(team_a)
    set_b = set(team_b)

    return {
        "common": set_a & set_b,
        "all_skills":set_a | set_b,
        "only A" : set_a - set_b,
        "only B" : set_b - set_a,

    }

"""Build nested dict structure from list of Student namedtuples."""

Student = namedtuple("Student",["name","score","city"])

def build_classroom (students: list[Student])-> dict[str, dict]:
    classroom={}

    for i, student in enumerate(students):
        stud_id = f"student_{i:03d}" # student_000, student_001, etc.
        avg = sum(student.score)/len(student.score)

        classroom[stud_id] = {
            "name"  : student.name,
            "score" : student.score,
            "avg" : round(avg,2),
            "grade" : gen_letter_grade(avg),
            "info" : {
                "city" : student.city
            }
        }
    return classroom

        

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


"""Return names of top N students by average score."""

def top_students(classroom: dict[str, dict], n: int = 3) -> list[str|None]:
    sorted_students = sorted (classroom.values(), key= lambda s: s["avg"], reverse = True)
    return [s.get("name") for s in sorted_students[:n]]


"""Count students per grade using dict comprehension."""

def grade_distribution (classroom : dict [str, dict])->dict [str, int]:
    grades = [s["grade"] for s in classroom.values()]
    return {grade : grades.count(grade) for grade in sorted(set(grades))}



if __name__ == "__main__":
    # Part 1
    print("=== Score Processing ===")
    raw_scores = [85, 92, 78, 92, 55, 78, 100, 63, 85]
    print(processed_scores(raw_scores))

    print("\n=== Skill Analysis ===")
    team_a = ["Python", "FastAPI", "Docker", "SQL"]
    team_b = ["Python", "LangChain", "Docker", "React"]
    result = skill_analysis(team_a, team_b)
    for key, val in result.items():
        print(f"{key}: {val}")

    # Part 2
    print("\n=== Student Grade System ===")
    students = [
        Student("Priyanshu", [92, 88, 95, 91], "Jaipur"),
        Student("Rahul",     [78, 82, 75, 80], "Delhi"),
        Student("Sneha",     [55, 60, 58, 62], "Mumbai"),
        Student("Amit",      [70, 68, 73, 71], "Pune"),
        Student("Divya",     [95, 98, 92, 97], "Bangalore"),
    ]

    classroom = build_classroom(students)

    for sid, data in classroom.items():
        print(f"{sid}: {data['name']} | Avg: {data['avg']} | Grade: {data['grade']}")

    print(f"\nTop 3: {top_students(classroom)}")
    print(f"Grade Distribution: {grade_distribution(classroom)}")



