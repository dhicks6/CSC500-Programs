Room_Num = {'CSC101': 3004, 'CSC102': 4501, 'CSC103': 6755, 'NET110': 1244, 'COM241': 1411}
Instructors = {'CSC101': 'Haynes', 'CSC102': 'Alvarado', 'CSC103': 'Rich', 'NET110': 'Burke', 'COM241': 'Lee'}
Meeting_Time = {'CSC101': '8:00 a.m.', 'CSC102': '9:00 a.m.', 'CSC103': '10:00 a.m.', 'NET110': '11:00 a.m.', 'COM241': '1:00 p,m,'}

Course_Name = input("What course would you like to see the information for?")
def print_course_info(course_name: str):
    if course_name in Room_Num and course_name in Instructors and course_name in Meeting_Time:
        print(f"Course: {course_name}")
        print(f"Room Number: {Room_Num[course_name]}")
        print(f"Instructor: {Instructors[course_name]}")
        print(f"Meeting Time: {Meeting_Time[course_name]}")
    else:
        print("Course not found.")
        
print_course_info(Course_Name)