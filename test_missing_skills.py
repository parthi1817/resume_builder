from data.career_data import career_db
from utils.missing_skills import get_missing_skills

user_skills = [
    "Python",
    "Java",
    "SQL",
    "Git",
    "DSA",
    "DBMS"
]

required_skills = career_db["Software Engineer"]["skills"]

missing = get_missing_skills(
    user_skills,
    required_skills
)

print(missing)