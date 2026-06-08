def analyze_weaknesses(missing_skills):

    weaknesses = []

    for skill in missing_skills:

        weaknesses.append(
            f"Lacks knowledge in {skill}"
        )

    return weaknesses