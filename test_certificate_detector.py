from utils.certificate_detector import detect_certificates

text = """
AWS Cloud Practitioner Certification
Google Data Analytics Certificate
Python Programming Course
"""

certificates = detect_certificates(text)

print(certificates)