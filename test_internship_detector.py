from utils.internship_detector import detect_internships

text = """
Software Development Intern at ABC Technologies
Completed internship in Python Development
Good communication skills
"""

internships = detect_internships(text)

print(internships)