from utils.section_extractor import extract_section


def detect_internships(lines):

    internship_lines = extract_section(
        lines,
        "INTERNSHIPEXPERIENCE",
        "CERTIFICATIONS"
    )

    internships = []

    for line in internship_lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("\uf0b7"):
            continue

        internships.append(line)

    return internships