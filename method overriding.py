import logging
logging.basicConfig(filename="method overriding.log", level=logging.INFO, format= '%(levelname)s %(asctime)s %(name)s %(message)s')


# Example 1
class ineuron3:
    logging.info("This is a class called ineuron3")
    try:
        logging.info("Creating different methods")
        def student_name3(self):
            print("List the names of all the student enrolled in ineuron3")
            logging.info("List the names of all the student enrolled in ineuron3")
        def no_of_courses3(self):
            print("List the number of courses each student is enrolled in")
            logging.info("List the number of courses each student is enrolled in")
    except Exception as e:
        logging.exception(e)
        print(e)

class ineuron_3:
    logging.info("This is another class called ineuron_3")
    try:
        logging.info("Creating an ovveriding method")
        def student_name3(self):
            print("List the names of only those students that are enrolled in the FSDS course")
            logging.info("List the names of only those students that are enrolled in the FSDS course")
    except Exception as e:
        logging.exception(e)
        print(e)

iv3 = ineuron3()
iv3.student_name3()
logging.info(iv3.student_name3())
iv_3 = ineuron_3()
iv_3.student_name3()
logging.info(iv_3.student_name3())



# Example 2
class student3:
    logging.info("This is a class called student3")
    try:
        logging.info("Creating different methods")
        def student_name3(self):
            print("List out all the names of the students")
            logging.info("List out all the names of the students")
        def enrollment_no3(self):
            print("List out the enrollment numbers of all the students")
            logging.info("List out the enrollment numbers of all the students")
        def id_no3(self):
            print("List out the id number of all the students")
            logging.info("List out the id number of all the students")
    except Exception as e:
        logging.exception(e)
        print(e)

class student_3:
    logging.info("This is another class called student_3")
    try:
        logging.info("Creating an overriding method")
        def id_no3(self):
            print("List out the id number of only those students whose id number ends with 3")
            logging.info("List out the id number of only those students whose id number ends with 3")
    except Exception as e:
        logging.exception(e)
        print(e)

s3 = student3()
s3.id_no3()
logging.info(s3.id_no3())
s_3 = student_3()
s_3.id_no3()
logging.info(s_3.id_no3())

# Example 3
class courses3:
    logging.info("This is a class called course3")
    try:
        logging.info("Creating different methods")

        def course_name3(self):
            print("List out all the names of the courses offered")
            logging.info("List out all the names of the courses offered")

        def no_of_courses3(self):
            print("List the total number of courses offered")
            logging.info("List the total number of courses offered")
    except Exception as e:
        loggin.exception(e)
        print(e)


class courses_3:
    logging.info("This is another class called courses_3")
    try:
        logging.info("Creating an overriding method")

        def course_name3(self):
            print("List the names that are being offered in this semester only")
            logging.info("List the names that are being offered in this semester only")
    except Exception as e:
        loggin.exception(e)
        print(e)


c3 = courses3()
c3.course_name3()
logging.info(c3.course_name3())
c_3 = courses_3()
c_3.course_name3()
logging.info(c3.course_name3())



# Example 4
class blogs3:
    logging.info("This is a class called blogs3")
    try:
        logging.info("Creating different methods")

        def blog_title3(self):
            print("List out all the blogs available on the website")
            logging.info("List out all the blogs available on the website")

        def no_of_blogs3(self):
            print("List out the total number of blogs on the website")
            logging.info("List out the total number of blogs on the website")
    except Exception as e:
        logging.exception(e)
        print(e)


class blogs_3:
    logging.info("This is another class called blog_3")
    try:
        logging.info("Creating an overriding method")

        def blog_title3(self):
            print("List out only the blogs related to Data Science")
            logging.info("List out only the blogs related to Data Science")
    except Exception as e:
        logging.exception(e)
        print(e)


b3 = blogs3()
b3.blog_title3()
logging.info(b3.blog_title3())
b_3 = blogs_3()
b_3.blog_title3()
logging.info(b_3.blog_title3())



# Example 5
class internship3:
    logging.info("This is a class called internship3")
    try:
        logging.info("Creating different methods")
        def student_name3(self):
            print("List out the names of all the students")
            logging.info("List out the names of all the students")
        def student_id_no3(self):
            print("List out the id number of all the students")
            logging.info("List out the id number of all the students")
        def internship_duration3(self):
            print("List out the internship duration of all the domains")
            logging.info("List out the internship duration of all the domains")
    except Exception as e:
        logging.exception(e)
        print(e)

class internship_3:
    logging.info("This is another class called internship_3")
    try:
        logging.info("Creating an overriding method")
        def students_name3(self):
            print("List out only the name of students that are eligible for internship")
            logging.info("List out only the name of students that are eligible for internship")
    except Exception as e:
        logging.exception(e)
        print(e)

intern3 = internship3()
intern3.student_name3()
logging.info(intern3.student_name3())
intern_3 = internship_3()
intern_3.students_name3()
logging.info(intern_3.students_name3())



# Example 6
class jobs3:
    logging.info("This is a class called jobs3")
    try:
        logging.info("Creating different methods")

        def emp_name3(self):
            print("List out the names of all the employees")
            logging.info("List out the names of all the employees")

        def emp_id3(self):
            print("List out the id numbers of all the employees")
            logging.info("List out the names of all the employees")

        def emp_salary3(self):
            print("List out the salary of all the employees")
            logging.info("List out the salary of all the employees")
    except Exception as e:
        logging.exception(e)
        print(e)


class jobs_3:
    logging.info("This is another class called jobs_3")
    try:
        logging.info("Creating an overriding method")

        def emp_salary3(self):
            print("List out the salaries of only the employees working in the data department")
            logging.info("List out the salaries of only the employees working in the data department")
    except Exception as e:
        logging.exception(e)
        print(e)


j3 = jobs3()
j3.emp_salary3()
logging.info(j3.emp_salary3())
j_3 = jobs_3()
logging.info(j_3.emp_salary3())



# Example 7
class affilates3:
    logging.info("This is a class called affilates3")
    try:
        logging.info("Creating different methods")

        def affilates_name3(self):
            print("List out the name of all the affilates")
            logging.info("List out the name of all the affilates")

        def no_of_affilates3(self):
            print("List the number of affilates")
            logging.info("List the number of affilates")
    except Exception as e:
        logging.exception(e)
        print(e)


class affilates_3:
    logging.info("This is another class called affilates_3")
    try:
        logging.info("Creating an overriding method")

        def affilates_name3(self):
            print("List out the name of affilates that are related to finance sector")
            logging.info("List out the name of affilates that are related to finance sector")

    except Exception as e:
        logging.exception(e)
        print(e)


a3 = affilates3()
a3.affilates_name3()
logging.info(a3.affilates_name3())
a_3 = affilates_3()
a_3.affilates_name3()
logging.info(a_3.affilates_name3())



# Example 8
class class_type3:
    logging.info("This is a class called class_type3")
    try:
        logging.info("Creating different methods")

        def student_name3(self):
            print("List out the names of all the students")
            logging.info("List out the names of all the students")

        def course_name3(self):
            print("List out the names of all the courses offered")
            logging.info("List out the names of all the courses offered")
    except Exception as e:
        logging.exception(e)
        print(e)


class class_type_3:
    logging.info("This is another class called class_type_3")
    try:
        logging.info("Creating an overriding method")

        def course_name3(self):
            print("List out only the name of courses that are being offered this semester")
            logging.info("List out only the name of courses that are being offered this semester")
    except Exception as e:
        logging.exception(e)
        print(e)


ct3 = class_type3()
ct3.course_name3()
logging.info(ct3.course_name3())
ct_3 = class_type_3()
ct_3.course_name3()
logging.info(ct_3.course_name3())



# Example 9
class student_portal3:
    logging.info("This is a class called student_portal3")
    try:
        logging.info("Creating different methods")
        def student_id3(self):
            print("List out the id number of all the students")
            logging.info("List out the id number of all the students")
        def student_password3(self):
            print("List out the passowards of all the students")
            logging.info("List out the passowards of all the students")
    except Exception as e:
        logging.exception(e)
        print(e)

class student_portal_3:
    logging.info("This is another class called student_portal_3")
    try:
        logging.info("Creating an overriding function")
        def student_id3(self):
            print("List out the id number of only those students that have registered for this session")
            logging.info("List out the id number of only those students that have registered for this session")
    except Exception as e:
        logging.exception(e)
        print(e)

st3 = student_portal3()
st3.student_id3()
logging.info(st3.student_id3())
st_3 = student_portal_3()
st_3.student_id3()
logging.info(st_3.student_id3())



# Example 10
class hackathon3:
    logging.info("This is a class called hackathon3")
    try:
        logging.info("Creating different methods")

        def team_name3(self):
            print("List out the names of all the teams")
            logging.info("List out the names of all the teams")

        def no_of_team_members3(self):
            print("List out the total number of team members")
            logging.info("List out the total number of team members")

        def project_title3(self):
            print("List out the all project titles")
            logging.info("List out the all project titles")
    except Exception as e:
        logging.exception(e)
        print(e)


class hackathon_3:
    logging.info("This is another class called hackathon_3")
    try:
        logging.info("Creating an overriding method")

        def no_of_team_members3(self):
            print("List out the number of team memebers in each team")
            logging.info("List out the number of team memebers in each team")
    except Exception as e:
        logging.exception(e)
        print(e)


hat3 = hackathon3()
hat3.no_of_team_members3()
logging.info(hat3.no_of_team_members3())
hat_3 = hackathon_3()
hat_3.no_of_team_members3()
logging.info(hat_3.no_of_team_members3())