from ai.feedback import generate_feedback

from ai.readiness import readiness_report

from ai.strengths import analyze_strengths

from ai.weakness import analyze_weaknesses

from ai.recommendation import (
    generate_recommendations
)


def generate_final_report(
    skills,
    missing_skills,
    ats_score,
    career
):

    report = {

        "feedback":
            generate_feedback(ats_score),

        "readiness":
            readiness_report(ats_score),

        "strengths":
            analyze_strengths(
                skills,
                career
            ),

        "weaknesses":
            analyze_weaknesses(
                missing_skills
            ),

        "recommendations":
            generate_recommendations(
                missing_skills,
                career
            )
    }

    return report