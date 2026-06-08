from utils.section_extractor import extract_section


def detect_certificates(lines):

    certificate_lines = extract_section(
        lines,
        "CERTIFICATIONS",
        "ACHIEVEMENTS"
    )

    certificates = []

    for line in certificate_lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("\uf0b7"):
            line = line.replace("\uf0b7", "").strip()

        certificates.append(line)

    return certificates