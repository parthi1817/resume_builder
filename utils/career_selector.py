# utils/career_selector.py

def select_career():

    print("\n===== SELECT DOMAIN =====")
    print("1. Engineering")
    print("2. Medical")
    print("3. Commerce")

    domain_choice = input("\nEnter choice: ")

    if domain_choice == "1":

        print("\n===== ENGINEERING CAREERS =====")
        print("1. Software Engineer")
        print("2. Web Developer")
        print("3. Data Analyst")
        print("4. Machine Learning Engineer")

        career_choice = input("\nSelect Career: ")

        engineering_careers = {
            "1": "Software Engineer",
            "2": "Web Developer",
            "3": "Data Analyst",
            "4": "Machine Learning Engineer"
        }

        return engineering_careers.get(
            career_choice,
            "Software Engineer"
        )

    elif domain_choice == "2":

        print("\n===== MEDICAL CAREERS =====")
        print("1. Doctor")
        print("2. General Physician")
        print("3. Surgeon")

        career_choice = input("\nSelect Career: ")

        medical_careers = {
            "1": "Doctor",
            "2": "General Physician",
            "3": "Surgeon"
        }

        return medical_careers.get(
            career_choice,
            "Doctor"
        )

    elif domain_choice == "3":

        print("\n===== COMMERCE CAREERS =====")
        print("1. Accountant")
        print("2. Auditor")
        print("3. Tax Consultant")

        career_choice = input("\nSelect Career: ")

        commerce_careers = {
            "1": "Accountant",
            "2": "Auditor",
            "3": "Tax Consultant"
        }

        return commerce_careers.get(
            career_choice,
            "Accountant"
        )

    else:

        print("\nInvalid choice.")
        print("Defaulting to Software Engineer.")

        return "Software Engineer"