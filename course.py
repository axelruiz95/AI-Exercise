def complete_courses():
    pending_courses = []

    for i in range(5):
        course = input(f"Enter the name of course {i + 1}: ")
        pending_courses.append(course)

    taken_courses = []
    for i in range(5):
        taken_course = input(f"Have you taken the course '{pending_courses[i]}'? (Yes/No): ").lower()
        if taken_course != 'yes':
            taken_courses.append(pending_courses[i])

    if taken_courses:
        print(f"You still need to take the course: {', '.join(taken_courses)}")
    else:
        print("Congratulations! You have completed all the courses.")

if __name__ == "__main__":
    complete_courses()
