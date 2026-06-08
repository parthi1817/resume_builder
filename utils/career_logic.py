from data.career_data import career_db

def missing_skills(user_skills, career):

    required_skills = career_db[career]["skills"]

    missing = []

    for skill in required_skills:
        if skill.lower() not in [s.lower() for s in user_skills]:
            missing.append(skill)

    return missing


def detect_domain(skills):

    skills = [skill.lower() for skill in skills]

    engineering = [
        "python", "java", "c++", "sql", "git",
        "html", "css", "javascript", "react",
        "node.js", "django", "flask",
        "dsa", "dbms", "oop",
        "operating systems", "computer networks",
        "machine learning", "linux", "mysql"
    ]

    medical = [
        "anatomy", "physiology", "pathology",
        "diagnosis", "patient care",
        "pharmacology", "clinical research",
        "medical ethics", "emergency medicine"
    ]

    commerce = [
        "accounting", "gst", "taxation",
        "tally", "excel", "auditing",
        "financial reporting", "bookkeeping",
        "budgeting"
    ]

    eng_count = sum(skill in skills for skill in engineering)
    med_count = sum(skill in skills for skill in medical)
    com_count = sum(skill in skills for skill in commerce)

    if eng_count >= med_count and eng_count >= com_count:
        return "Engineering"

    elif med_count >= eng_count and med_count >= com_count:
        return "Medical"

    else:
        return "Commerce"