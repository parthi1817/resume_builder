from utils.section_extractor import extract_section

def detect_projects(lines):

    project_lines = extract_section(
        lines,
        "PROJECTS",
        "INTERNSHIPEXPERIENCE"
    )

    projects = []

    for line in project_lines:

        line = line.strip()

        if not line:
            continue

        if "TechStack" in line:
           line = line.split("TechStack")[0]

           line = line.strip()

        if line.startswith("\uf0b7"):
            continue

        projects.append(line)

    return projects