# ========== File1 ==========

# Importing the permitted libraries.
import requests
import json

# Function to add the Student to Firebase Realtime Database.
def add(student_id, student_name, student_program):
    # Load the Firebase Realtime DB URL stored in the config file.
    with open("config.json") as cfr:
        config_data = json.load(cfr)
    url = config_data["url"]

    # Appending additional strings to the main URL to point towards the student data.
    url_split = url.split('.json')
    url = url_split[0] + "course_management_app/students/.json"

    # The data to be added for the mentioned student ID.
    data = {student_id:{"name": student_name, "program": student_program}}

    # Uploading the data to Firebase Realtime Database.
    # The reason I have used a patch request here is because, the patch request will take care- 
    # of addition of new student details as well as updating the existing student IDs details.
    requests.patch(url, data=json.dumps(data))
