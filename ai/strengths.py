def analyze_strengths(skills, career):

    strengths = []

    skills = [s.lower() for s in skills]

    if career == "Software Engineer":

        if "python" in skills:
            strengths.append("Good Python knowledge")

        if "sql" in skills:
            strengths.append("Understands database concepts")

        if "git" in skills:
            strengths.append("Familiar with version control")


    elif career == "Doctor":

        if "anatomy" in skills:
            strengths.append("Strong anatomy knowledge")

        if "patient care" in skills:
            strengths.append("Good patient care skills")

        if "diagnosis" in skills:
            strengths.append("Understands diagnosis process")


    elif career == "Accountant":

        if "gst" in skills:
            strengths.append("Good GST knowledge")

        if "excel" in skills:
            strengths.append("Strong Excel skills")

        if "taxation" in skills:
            strengths.append("Understands taxation concepts")

    return strengths