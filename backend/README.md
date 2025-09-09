
#📌 Relational Mapping Summary

---

Student – Course

- One student belongs to one course.
- One course has many students.

---

Course – Department

- One course belongs to one department.
- One department has many courses.

---

Section – Course

- One section belongs to one course.
- One course has many sections.

---

Subject – Subject (Prerequisite)

- One subject may have zero or one prerequisite.
- One subject can be a prerequisite for many other subjects.

---

Schedule – Teacher

- One schedule is handled by one teacher.
- One teacher can handle many schedules.

---

Schedule – Subject

- One schedule is for one subject.
- One subject can have many schedules (different sections, different teachers).

---

Schedule – Section

- One schedule is for one section.
- One section can have many schedules (its subjects across the semester).

---

Enrollment – Student

- One enrollment record belongs to one student.
- One student can have many enrollment records (different semesters).

---

Enrollment – Section

- One enrollment record belongs to one section (for regular students).
- One section can have many enrollment records (students enrolled in that section).
- ⚠️ For irregular students → section may be NULL or linked to a special “Irregular” section.

---

Enrollment_Detail – Enrollment

- One enrollment detail belongs to one enrollment record.
- One enrollment record can have many enrollment details (the subjects the student takes).

---

Enrollment_Detail – Schedule

- One enrollment detail is tied to one schedule.
- One schedule can appear in many enrollment details (because many students can enroll in it).

---

Payment – Student

- One payment belongs to one student.
- One student can have many payments (installments, multiple semesters).

---

Student_Requirement – Student & Requirement (M:N)

- One student can have many requirements.
- One requirement can apply to many students.
- Student_Requirement acts as the bridge table that records submission status and dates.

---

## Crow’s foot style notation:

### 📌 Relational Mapping Quick Reference

```
Student  ∞—1  Course
Course   ∞—1  Department
Section  ∞—1  Course
Subject  ∞—0..1 Subject   (self-reference for prerequisite)
Schedule ∞—1  Teacher
Schedule ∞—1  Subject
Schedule ∞—1  Section
Enrollment ∞—1 Student
Enrollment ∞—0..1 Section  (NULL for irregulars)
Enrollment_Detail ∞—1 Enrollment
Enrollment_Detail ∞—1 Schedule
Payment ∞—1 Student
Student_Requirement ∞—1 Student
Student_Requirement ∞—1 Requirement
```
