# ========== File3 ==========

# Importing the permitted libraries.
import requests
import json

# Function to add the Student to Firebase Realtime Database.
def add(course_number, course_title, course_semester):
    # Load the Firebase Realtime DB URL stored in the config file.
    with open("config.json") as cfr:
        config_data = json.load(cfr)
    url = config_data["url"]

    # Appending additional strings to the main URL to point towards the instructor data.
    url_split = url.split('.json')
    url = url_split[0] + "course_management_app/courses/.json"

    # Retrieving the course data to update the additional details.
    response = requests.get(url)
    data = response.json()

    # If course section does not exists, this condition is handled by IF block.
    if data == None:
        data = {course_number:{"semester":{course_semester:True}, "title":course_title}}
    # If course section exists, but the course number given in the input is not present, this is handled by ELIF block.
    elif data.get(course_number) == None:
        data = {course_number:{"semester":{course_semester:True}, "title":course_title}}
    # If the course number exists, the data addition is handled by ELSE block.
    else:
        data[course_number]["semester"][course_semester] = True

    # Uploading the data to Firebase Realtime Database.
    # The reason I have used a patch request here is because, the patch request will take care- 
    # of addition of new course details as well as updating the existing course number details.
    requests.patch(url, data=json.dumps(data))
