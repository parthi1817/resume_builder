from data.interview_questions import interview_questions

def get_interview_questions(career):

    return interview_questions.get(
        career,
        ["No questions available"]
    )