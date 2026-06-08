def detect_internships(text):

    internship_keywords = [
        "intern",
        "internship",
        "trainee",
        "apprentice",
        "industrial training"
    ]

    found_internships = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.lower() == "internships/experience":
            continue

        for keyword in internship_keywords:

            if keyword in line.lower():

                if line not in found_internships:
                    found_internships.append(line)

                break

    return found_internships