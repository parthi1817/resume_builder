from rapidfuzz import process

skills_db = [
    "python",
    "java",
    "javascript",
    "django",
    "flask"
]

word = "djagno"

match = process.extractOne(word, skills_db)

print(match)