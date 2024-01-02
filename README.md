# Course Management Application for University using Firebase Real-time Database

![image](https://github.com/prathmeshlonkar10/Course-Management-Application-for-University/assets/66990159/6ec0d631-086b-4a73-b1aa-ebd0d3d75655)


## Highlight
This simple project consists of an application for managing courses for the University. For the backend, the Firebase real-time database has been used to store and manage the data of the application. The database stores the following information about students, instructors, courses, and their relationships.

-	Student: ID(e.g., "s100"), Name(e.g., "Patrick Jane"), and Program(e.g., "Applied Data Science"). 
-	Instructor: ID(e.g., "i100"), Name(e.g., "Jessica Pearson"), and Department(e.g., "Statistics").
-	Course: Number(e.g., "DSCI 551"), Title(e.g., "Foundations of Data Management"), and Semester(e.g., "Fall 2023").
-	Relationships: Students take Courses, and Instructors teach Courses.

A student can take multiple courses in multiple semesters and an instructor can teach a course in multiple semesters. Accordingly, the data for Students and Instructors can be associated with data for Courses to form relationships.


## Technologies used
![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![](https://img.shields.io/badge/JSON-000000.svg?style=for-the-badge&logo=JSON&logoColor=white)
![](https://img.shields.io/badge/Firebase-FFCA28.svg?style=for-the-badge&logo=Firebase&logoColor=black)


## Actions
- Add Data: This action is used to add new data for student, instructor, or course by providing the parameters given above
- Associate Data: This action builds a "Student takes Course" or an "Instructor teaches Course" relationship.
- Fetch Data: This action retrieves all the data for the selected Student or Instructor


## Future Scope
- Deletion of data
- Update data
- Course data fetch

