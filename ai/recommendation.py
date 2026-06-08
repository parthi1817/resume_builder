def generate_recommendations(
    missing_skills,
    career
):

    recommendations = []

    for skill in missing_skills:

        if career == "Software Engineer":

            if skill == "DBMS":
                recommendations.append(
                    "Learn SQL, normalization, and database design."
                )

            elif skill == "OOP":
                recommendations.append(
                    "Practice classes, inheritance, polymorphism, and abstraction."
                )

            elif skill == "DSA":
                recommendations.append(
                    "Practice arrays, linked lists, trees, and problem solving."
                )

            else:
                recommendations.append(
                    f"Improve knowledge in {skill}."
                )


        elif career == "Doctor":

            recommendations.append(
                f"Improve understanding of {skill} through clinical practice."
            )


        elif career == "Accountant":

            recommendations.append(
                f"Practice and improve {skill} concepts."
            )

    return recommendations