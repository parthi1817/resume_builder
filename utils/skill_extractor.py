def extract_skills(text):
    skills_db = [
        "python", "java", "c++", "sql",
        "machine learning", "data analysis",
        "html", "css", "javascript",
        "react", "node", "django", "flask"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills