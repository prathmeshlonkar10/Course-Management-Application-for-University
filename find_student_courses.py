# ========== File6 ==========

# Importing the permitted libraries.
import requests
import json

def fetch(student_id):
  # Load the Firebase Realtime DB URL stored in the config file.
  with open("config.json") as cfr:
      config_data = json.load(cfr)
  url = config_data["url"]

  # Appending additional strings to the main URL to point towards the data.
  url_split = url.split('.json')
  url = url_split[0] + "course_management_app/relationships/students/{}.json".format(student_id)

  # Capture the response from Firebase.
  response = requests.get(url)

  # Error Handling for data retreival.
  if response.status_code == 200:
    # The request was successful, hence converting to json format.
    data = response.json()
    if data == None:       
      print("\n========== ERROR ==========\nProvided Student ID {} has no associated course data. Please associate this Student ID with available Courses and try again.".format(student_id))
      return False
  else:
    # The request failed, hence quiting the script.
    print("\n========== ERROR ==========\nUnable to fetch data from Firebase: {}".format(response.status_code))
    return False

  # Print the data if successfully captured.
  print("\n========== SUCCESS ==========\nData Successully fetched for student ID {0}. The student name and the list of courses taken by the student is as follows:\n".format(student_id), json.dumps(data, indent=2))
  return True
