import re
from data.skill_aliases import SKILL_ALIASES
from rapidfuzz import process

def extract_skills(text):

    skills_db = [

        "python",
        "java",
        "c++",
        "sql",
        "git",
        "dsa",
        "dbms",
        "oop",
        "operating systems",
        "computer networks",
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "django",
        "flask",
        "machine learning",
        "data analysis",
        "rest api",
        "mongodb",
        "mysql",
        "postgresql",
        "linux",
        "docker",
        "aws",
        "github",
        "testing",
        "debugging",
        "problem solving",

        "anatomy",
        "physiology",
        "pathology",
        "diagnosis",
        "patient care",
        "pharmacology",
        "clinical research",
        "medical ethics",
        "emergency medicine",

        "accounting",
        "gst",
        "taxation",
        "tally",
        "excel",
        "auditing",
        "financial reporting",
        "bookkeeping",
        "budgeting"
    ]

    found_skills = set()

    text = text.lower()
    

    # Exact matches
    for skill in skills_db:
        if skill in text:
            found_skills.add(skill)

    # Fuzzy matches


    text = re.sub(r'[^\w\s.+#]', ' ', text.lower())
    words = text.split()
    
    for word in words:

        match = process.extractOne(word, skills_db)

        if match and match[1] >= 80:
            found_skills.add(match[0])
    for main_skill, aliases in SKILL_ALIASES.items():

     for main_skill, aliases in SKILL_ALIASES.items():
         for alias in aliases:

             if alias.lower() in text:
                 found_skills.add(main_skill)

    return list(found_skills)