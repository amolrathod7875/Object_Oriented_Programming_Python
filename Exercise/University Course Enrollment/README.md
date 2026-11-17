# University Course Enrollment

## Overview

Day 02 challenge: a university enrollment system demonstrating **many-to-many relationships** and invariants. `Student` and `Course` are plain entities; `University` owns the enrollment state, tracking which students are enrolled in each course and enforcing capacity and uniqueness rules.

## Tasks

- [x] Create `Student`, `Course(capacity)` and `University` classes.
- [x] Implement `enroll(student_id, course_id)`, `drop(...)`, and `list_enrollments(...)`.
- [x] Reject duplicate enrollments, unknown IDs and full courses.

## Pass Checks

- [x] A course with capacity 2 accepts two students and rejects a third.
- [x] Dropping a student makes one place available.
- [x] The same student cannot enroll twice.

## Code

```python
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

class Course:
    def __init__(self, course_id, name, capacity):
        if capacity <= 0:
            raise ValueError("Invalid Course Capacity")
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

    def drop(self, student_id, course_id):
        if student_id not in self.students:
            raise ValueError("Student Does Not Exist")
        if course_id not in self.courses:
            raise ValueError("Course Does Not Exist")
        course = self.courses[course_id]
        if student_id not in course.enrolled_students:
            raise ValueError("Student Is Not Enrolled")
        course.enrolled_students.remove(student_id)

    def list_enrollments(self, course_id):
        if course_id not in self.courses:
            raise ValueError("Course Does Not Exist")
        course = self.courses[course_id]
        print(f"Course: {course.name}")
        print(f"Capacity: {course.capacity}")
        print(f"Enrolled: {len(course.enrolled_students)}")
        for student_id in sorted(course.enrolled_students):
            student = self.students[student_id]
            print(f"{student.student_id} - {student.name}")
```

## How the Code Satisfies the Tasks

- **Entities**: `Student` (id, name) and `Course` (id, name, capacity, enrolled set).
- **University**: registry of students and courses; enrollment state lives on each `Course`.
- **enroll**: validates student and course existence, rejects duplicates and full courses, then adds the student.
- **drop**: validates existence and enrollment, then removes the student, freeing capacity.
- **list_enrollments**: prints course metadata and enrolled students.

## Sample Behavior

```python
uni = University()
uni.add_student(Student(101, "Amol"))
uni.add_student(Student(102, "Rahul"))
uni.add_courses(Course("CS101", "Python", 2))

uni.enroll(101, "CS101")
uni.enroll(102, "CS101")   # full
# uni.enroll(103, "CS101")  # raises "Course Capacity Is Full"
uni.drop(101, "CS101")
uni.enroll(103, "CS101")   # succeeds after drop
```

## Running the example

```bash
cd "Exercise/University Course Enrollment"
python code.py
```

## Interview Questions

1. **Where should enrollment rules live — Student, Course, or University?**
   In the `University` (or a dedicated enrollment service). It is the aggregate root that knows about both students and courses and can enforce cross-entity invariants like capacity and duplicate checks.

2. **How do you model a many-to-many relationship in Python?**
   Either with a join collection (e.g., a set of `(student_id, course_id)` tuples) or by storing enrolled sets on both sides. Here each `Course` keeps an `enrolled_students` set, which keeps capacity checks O(1).

3. **How do you prevent a student from enrolling twice in the same course?**
   Check membership in `course.enrolled_students` before adding; raise if already present. A `set` makes this O(1).

4. **What happens to capacity when a student drops?**
   Removing the student from `enrolled_students` decrements the count, freeing a slot for future enrollments without any separate counter to keep in sync.

5. **How would you support listing all courses a student is enrolled in?**
   Maintain a reverse mapping `student_id -> set of course_ids` (or derive it by scanning courses). This trades extra memory for O(1) lookup of a student's schedule.
