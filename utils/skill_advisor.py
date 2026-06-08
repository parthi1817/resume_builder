from data.skill_info import skill_info

def explain_missing_skills(missing_skills):

    advice = {}

    for skill in missing_skills:

        if skill in skill_info:
            advice[skill] = skill_info[skill]

        else:
            advice[skill] = "No information available."

    return advice