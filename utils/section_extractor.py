def extract_section(lines, start_header, end_header):
    section = []
    capture = False

    for line in lines:

        if start_header in line.upper():
            capture = True
            continue

        if capture and end_header in line.upper():
            break

        if capture:
            section.append(line)

    return section