from data.career_data import career_db

def calculate_ats(
    user_skills,
    career,
    projects=None,
    internships=None,
    certificates=None
):

    if projects is None:
        projects = []

    if internships is None:
        internships = []

    if certificates is None:
        certificates = []

    required_skills = career_db[career]["skills"]

    matched_skills = 0

    for skill in required_skills:

        if skill.lower() in [s.lower() for s in user_skills]:
            matched_skills += 1

    # Skills = 60 marks
    skills_score = (
        matched_skills / len(required_skills)
    ) * 60

    # Projects = 15 marks
    project_score = min(len(projects) * 5, 15)

    # Internships = 15 marks
    internship_score = min(len(internships) * 15, 15)

    # Certificates = 10 marks
    certificate_score = min(len(certificates) * 5, 10)

    total_score = (
        skills_score
        + project_score
        + internship_score
        + certificate_score
    )

    return round(total_score, 2)