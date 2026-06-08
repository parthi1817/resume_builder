def readiness_report(ats_score):

    if ats_score >= 80:

        return "High Job Readiness"

    elif ats_score >= 60:

        return "Moderate Job Readiness"

    else:

        return "Low Job Readiness"