def detect_projects(text):

    project_keywords = [
        "project",
        "developed",
        "built",
        "created",
        "implemented",
        "designed"
    ]

    found_projects = []

    lines = text.split("\n")

    for line in lines:

        line_lower = line.lower()

        print(repr(line))
        
        for keyword in project_keywords:

            if keyword in line_lower:
                found_projects.append(line.strip())
                break

    return found_projects