from data.roadmap_data import roadmap_data

def get_roadmap(career):

    return roadmap_data.get(
        career,
        ["No roadmap available"]
    )