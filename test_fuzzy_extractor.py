from rapidfuzz import process

skills_db = [
    "python",
    "java",
    "javascript",
    "django",
    "flask"
]

resume_words = [
    "pyton",
    "javscript",
    "djagno",
    "python"
]

found_skills = set()

for word in resume_words:

    match = process.extractOne(word, skills_db)

    if match and match[1] >= 80:
        found_skills.add(match[0])

print(list(found_skills))