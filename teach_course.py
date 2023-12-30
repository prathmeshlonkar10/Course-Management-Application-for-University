# ========== File5 ==========

# Importing the permitted libraries.
import requests
import json

# Function to Assign Student with Course.
def teach(instructor_id, course_number, course_semester):
    # Load the Firebase Realtime DB URL stored in the config file.
    with open("config.json") as cfr:
        config_data = json.load(cfr)
    url = config_data["url"]

    # Appending additional strings to the main URL to point towards the data.
    url_split = url.split('.json')
    validate_url = url_split[0] + "course_management_app/.json"

    # Retrieving data to validate the user input.
    response = requests.get(validate_url)
    data = response.json()

    # Validating the user input.
    try:
        data["instructors"][instructor_id]
        print("\nNote: Instructor ID check successful.")   
        data["courses"][course_number]
        print("\nNote: Course Number check successful.")   
        data["courses"][course_number]["semester"][course_semester]
        print("\nNote: Course Semester check successful.")   
    except:
        print("\n========== ERROR ==========\nThe provided user input(s) does not exist in the database. Please verify and retry!\n")
        return False

    # Retrieveing Instructor name to add into relationships and then creating relationship URL.
    instructor_name = data["instructors"][instructor_id]["name"]
    relationships_url = url_split[0] + "course_management_app/relationships/instructors/{0}/.json".format(instructor_id)

    # Retrieving the relationship data to update the additional details.
    response = requests.get(relationships_url)
    relationships_data = response.json()

    # If relationship section or any further sections do not exist, this condition is handled by IF block.
    # This block adds new course details from scratch.
    if relationships_data == None:
        relationships_data = {"name":instructor_name, "courses":{course_number:{"semester":{course_semester:True}}}}

    # If relationship or further sections exist, but the course number given in the input is not present, this is handled by ELIF block.
    # This block adds new course details if others are already present.
    elif relationships_data["courses"].get(course_number) == None:
        relationships_url = relationships_url.split('.json')[0] + "courses/.json"
        relationships_data = {course_number:{"semester":{course_semester:True}}}

    # If the course number exists, the data addition is handled by ELSE block.
    # This block adds a semester entry to current course. Eg: If an Instructor teaches a course again in next semester.
    else:
        relationships_data["courses"][course_number]["semester"][course_semester] = True

    # Uploading the data to Firebase Realtime Database.
    # The reason I have used a patch request here is because, the patch request will take care- 
    # of addition of new course details as well as updating the existing course details.
    requests.patch(relationships_url, data=json.dumps(relationships_data))
    return True