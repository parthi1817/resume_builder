def detect_certificates(text):

    certificate_keywords = [
        "certificate",
        "certification",
        "certified",
        "course",
        "credential"
    ]

    found_certificates = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        for keyword in certificate_keywords:

            if keyword in line.lower():

                if line not in found_certificates:
                    found_certificates.append(line)

                break

    return found_certificates