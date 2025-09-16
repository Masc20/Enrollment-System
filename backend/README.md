=====================================
## 📌 Relational Mapping Summary (Updated)
=====================================

**1. Student – Enrollment (1:M)**
   - A student can have multiple enrollments (per academic year/semester).
   - Each enrollment belongs to exactly one student.
   - The course and section are tracked here (students can shift courses or sections).

**2. Enrollment – Enrollment_Detail (1:M)**
   - An enrollment can have many enrollment details (one per subject/schedule).
   - Each detail belongs to exactly one enrollment.

**3. Enrollment_Detail – Schedule (M:1)**
   - Each enrollment detail links to one schedule.
   - A schedule can be linked by many enrollment details (many students in the same class).

**4. Schedule – Teacher (M:1)**
   - Each schedule is taught by one teacher.
   - A teacher can teach multiple schedules.

**5. Schedule – Subject (M:1)**
   - Each schedule is for one subject.
   - A subject can appear in multiple schedules (different sections/semesters).

**6. Schedule – Section (M:1)**
   - Each schedule belongs to one section.
   - A section can have many schedules.
   - Irregulars are placed in a special "Irregular Section" instead of NULL.

**7. Section – Course (M:1)**
   - Each section is tied to one course.
   - A course can have multiple sections.

**8. Course – Department (M:1)**
   - Each course belongs to one department.
   - A department can offer many courses.

**9. Subject – Subject (1:M self-relationship)**
   - A subject can have prerequisites.
   - Example: Calculus 2 requires Calculus 1.

**10. Requirement – Student (M:N via Student_Requirement)**
    - A requirement can apply to many students.
    - A student can submit many requirements.

**11. Payment – Enrollment (1:M)**
    - Each payment belongs to one enrollment (semester-based).
    - An enrollment can have multiple payments.
    - Ensures tuition tracking per semester.

**12. Grade – Enrollment_Detail (M:1)**
    - Each grade is tied to one enrollment detail (a student’s subject).
    - Stores numeric grade and remarks per subject per semester.

---

=====================================
## 📝 Compact Crow’s Foot Notation (Updated)
=====================================


- Student              ∞—1   Enrollment
- Enrollment           ∞—1   Course
- Course               ∞—1   Department
- Section              ∞—1   Course		( "Course"-"Section ) || ("Course"-IRREG)
- Subject              ∞—0..1 Subject		(self-reference for prerequisite)

- Schedule             ∞—1   Teacher
- Schedule             ∞—1   Subject
- Schedule             ∞—1   Section

- Enrollment_Detail    ∞—1   Enrollment
- Enrollment_Detail    ∞—1   Schedule

- Grade                ∞—1   Enrollment_Detail

- Payment              ∞—1   Enrollment

- Student_Requirement  ∞—1   Student
- Student_Requirement  ∞—1   Requirement

