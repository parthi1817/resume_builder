def generate_feedback(ats_score):

    if ats_score >= 80:

        return (
            "Strong resume with good job readiness."
        )

    elif ats_score >= 60:

        return (
            "Good resume but needs some improvements."
        )

    else:

        return (
            "Resume needs major improvement before applying."
        )