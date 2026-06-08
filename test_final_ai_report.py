from ai.final_report import (
    generate_final_report
)

skills = [
    "python",
    "sql",
    "git"
]

missing_skills = [
    "DSA",
    "OOP",
    "DBMS"
]

ats_score = 72

career = "Software Engineer"

report = generate_final_report(
    skills,
    missing_skills,
    ats_score,
    career
)

print(report)