import csv
import argparse

def read_courses(filename):
    courses = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            courses.append(row)

    return courses


def display_courses(courses):
    print("\nAll Course Records:")
    print("-" * 60)

    for course in courses:
        print("Course ID :", course["CourseID"])
        print("Course Name :", course["CourseName"])
        print("Instructor :", course["Instructor"])
        print("Credits :", course["Credits"])
        print("-" * 60)


def search_course(courses, course_id):
    for course in courses:
        if course["CourseID"] == course_id:
            print("\nCourse Found:")
            print("Course ID :", course["CourseID"])
            print("Course Name :", course["CourseName"])
            print("Instructor :", course["Instructor"])
            print("Credits :", course["Credits"])
            return

    print("\nCourse not found.")


parser = argparse.ArgumentParser(
    description="Course Information System"
)

parser.add_argument(
    "filename",
    help="CSV file containing course details"
)

args = parser.parse_args()

courses = read_courses(args.filename)

display_courses(courses)

course_id = input("\nEnter Course ID to search: ")
search_course(courses, course_id)