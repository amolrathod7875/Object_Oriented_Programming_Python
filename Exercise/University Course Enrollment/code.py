
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


class Course:
    def __init__(self, course_id, name, capacity):
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.enrolled_students = set()


class University:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student):
        if student.student_id in self.students:
            raise ValueError("Student Already Exists")

        self.students[student.student_id] = student

    def add_courses(self, course):
        if course.course_id in self.courses:
            raise ValueError("Course Already Exists")

        if course.capacity <= 0:
            raise ValueError("Invalid Course Capacity")

        self.courses[course.course_id] = course

    def enroll(self, student_id, course_id):
        if student_id not in self.students:
            raise ValueError("Student Does Not Exist")

        if course_id not in self.courses:
            raise ValueError("Course Does Not Exist")

        course = self.courses[course_id]

        if student_id in course.enrolled_students:
            raise ValueError("Student Already Enrolled")

        if len(course.enrolled_students) >= course.capacity:
            raise ValueError("Course Capacity Is Full")

        course.enrolled_students.add(student_id)
        print("Student Enrolled Successfully")

    def drop(self, student_id, course_id):
        if student_id not in self.students:
            raise ValueError("Student Does Not Exist")

        if course_id not in self.courses:
            raise ValueError("Course Does Not Exist")

        course = self.courses[course_id]

        if student_id not in course.enrolled_students:
            raise ValueError("Student Is Not Enrolled")

        course.enrolled_students.remove(student_id)
        print("Student Dropped Successfully")

    def list_enrollments(self, course_id):
        if course_id not in self.courses:
            raise ValueError("Course Does Not Exist")

        course = self.courses[course_id]

        print(f"\nCourse: {course.name}")
        print(f"Capacity: {course.capacity}")
        print(f"Enrolled: {len(course.enrolled_students)}")
        print("Enrolled Students:")

        if not course.enrolled_students:
            print("No Students Enrolled")
            return

        for student_id in sorted(course.enrolled_students):
            student = self.students[student_id]
            print(f"{student.student_id} - {student.name}")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

uni = University()

# Create students
s1 = Student(101, "Amol")
s2 = Student(102, "Rahul")
s3 = Student(103, "Amit")

# Create courses
c1 = Course("CS101", "Python", 2)
c2 = Course("CS102", "DBMS", 3)

# Register students
uni.add_student(s1)
uni.add_student(s2)
uni.add_student(s3)

# Register courses
uni.add_courses(c1)
uni.add_courses(c2)

# Test 1: Enroll students
uni.enroll(101, "CS101")
uni.enroll(102, "CS101")

# Test 2: List enrollments
uni.list_enrollments("CS101")

# Test 3: Course capacity
try:
    uni.enroll(103, "CS101")
except ValueError as e:
    print("Error:", e)

# Test 4: Duplicate enrollment
try:
    uni.enroll(101, "CS101")
except ValueError as e:
    print("Error:", e)

# Test 5: Drop student
uni.drop(101, "CS101")

# Test 6: Enroll after dropping
uni.enroll(103, "CS101")

# Test 7: Final enrollments
uni.list_enrollments("CS101")

# Test 8: Many-to-many relationship
uni.enroll(102, "CS102")
uni.enroll(103, "CS102")

uni.list_enrollments("CS102")
