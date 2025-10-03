CREATE TABLE "Student" (
  "student_id" int PRIMARY KEY,
  "student_number" varchar(30),
  "first_name" varchar(30),
  "middle_name" varchar(30),
  "last_name" varchar(30),
  "birth_date" date,
  "gender" varchar(30),
  "contact_number" varchar(15),
  "email" varchar(50),
  "address" text,
  "admission_status" varchar(30),
  "enrollment_status" varchar(30)
);

CREATE TABLE "Teacher" (
  "teacher_id" int PRIMARY KEY,
  "first_name" varchar(30),
  "last_name" varchar(30),
  "contact_number" varchar(15),
  "email" varchar(50)
);

CREATE TABLE "Course" (
  "course_id" int PRIMARY KEY,
  "course_code" varchar(10),
  "course_name" varchar(50),
  "dept_id" int
);

CREATE TABLE "Department" (
  "dept_id" int PRIMARY KEY,
  "dept_name" varchar(50)
);

CREATE TABLE "Section" (
  "section_id" int PRIMARY KEY,
  "sec_name" varchar(30),
  "year_level" varchar(10),
  "course_id" int
);

CREATE TABLE "Subject" (
  "subject_id" int PRIMARY KEY,
  "sub_code" varchar(10),
  "subject_name" varchar(50),
  "sub_type" varchar(30),
  "num_units" int(2),
  "pre_req_id" int
);

CREATE TABLE "Schedule" (
  "schedule_id" int PRIMARY KEY,
  "days" varchar(30),
  "sched_time" timestamp,
  "room_number" varchar(10),
  "section_id" int,
  "subject_id" int,
  "teacher_id" int
);

CREATE TABLE "Enrollment" (
  "enrollment_id" int PRIMARY KEY,
  "academic_year" varchar(10),
  "semester" varchar(10),
  "year_level" varchar(10),
  "student_id" int,
  "section_id" int,
  "course_id" int
);

CREATE TABLE "Enrollment_Detail" (
  "enroll_detail_id" int PRIMARY KEY,
  "enrollment_id" int,
  "schedule_id" int
);

CREATE TABLE "Payment" (
  "payment_id" int PRIMARY KEY,
  "amount" double,
  "date_paid" datetime,
  "payment_method" varchar(30),
  "remarks" text,
  "enrollment_id" int
);

CREATE TABLE "Requirement" (
  "req_id" int PRIMARY KEY,
  "req_name" varchar(50)
);

CREATE TABLE "Student_Requirement" (
  "stud_req_id" int PRIMARY KEY,
  "status" varchar(10),
  "date_submitted" datetime,
  "stud_id" int,
  "req_id" int
);

CREATE TABLE "Grade" (
  "grade_id" int PRIMARY KEY,
  "grade" decimal(3,2),
  "remarks" varchar(30),
  "enroll_detail_id" int
);

ALTER TABLE "Course" ADD FOREIGN KEY ("dept_id") REFERENCES "Department" ("dept_id");

ALTER TABLE "Section" ADD FOREIGN KEY ("course_id") REFERENCES "Course" ("course_id");

ALTER TABLE "Subject" ADD FOREIGN KEY ("subject_id") REFERENCES "Subject" ("pre_req_id");

ALTER TABLE "Schedule" ADD FOREIGN KEY ("teacher_id") REFERENCES "Teacher" ("teacher_id");

ALTER TABLE "Schedule" ADD FOREIGN KEY ("subject_id") REFERENCES "Subject" ("subject_id");

ALTER TABLE "Schedule" ADD FOREIGN KEY ("section_id") REFERENCES "Section" ("section_id");

ALTER TABLE "Enrollment" ADD FOREIGN KEY ("student_id") REFERENCES "Student" ("student_id");

ALTER TABLE "Enrollment" ADD FOREIGN KEY ("section_id") REFERENCES "Section" ("section_id");

ALTER TABLE "Enrollment" ADD FOREIGN KEY ("course_id") REFERENCES "Course" ("course_id");

ALTER TABLE "Enrollment_Detail" ADD FOREIGN KEY ("enrollment_id") REFERENCES "Enrollment" ("enrollment_id");

ALTER TABLE "Enrollment_Detail" ADD FOREIGN KEY ("schedule_id") REFERENCES "Schedule" ("schedule_id");

ALTER TABLE "Payment" ADD FOREIGN KEY ("enrollment_id") REFERENCES "Enrollment" ("enrollment_id");

ALTER TABLE "Student_Requirement" ADD FOREIGN KEY ("stud_id") REFERENCES "Student" ("student_id");

ALTER TABLE "Student_Requirement" ADD FOREIGN KEY ("req_id") REFERENCES "Requirement" ("req_id");

ALTER TABLE "Grade" ADD FOREIGN KEY ("enroll_detail_id") REFERENCES "Enrollment_Detail" ("enroll_detail_id");
