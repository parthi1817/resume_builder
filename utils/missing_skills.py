def get_missing_skills(user_skills, required_skills):

    missing_skills = []

    user_skills_lower = [skill.lower() for skill in user_skills]

    for skill in required_skills:

        if skill.lower() not in user_skills_lower:
            missing_skills.append(skill)

    return missing_skills