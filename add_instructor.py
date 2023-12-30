# ========== File2 ==========

# Importing the permitted libraries.
import requests
import json

# Function to add the Student to Firebase Realtime Database.
def add(instructor_id, instructor_name, instructor_department):
    # Load the Firebase Realtime DB URL stored in the config file.
    with open("config.json") as cfr:
        config_data = json.load(cfr)
    url = config_data["url"]

    # Appending additional strings to the main URL to point towards the instructor data.
    url_split = url.split('.json')
    url = url_split[0] + "course_management_app/instructors/.json"

    # The data to be added for the mentioned instructor ID.
    data = {instructor_id:{"name": instructor_name, "department": instructor_department}}

    # Uploading the data to Firebase Realtime Database.
    # The reason I have used a patch request here is because, the patch request will take care- 
    # of addition of new instructor details as well as updating the existing instructor IDs details.
    requests.patch(url, data=json.dumps(data))
