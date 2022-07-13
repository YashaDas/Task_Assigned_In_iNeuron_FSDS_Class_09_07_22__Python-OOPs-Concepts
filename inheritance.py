import logging
logging.basicConfig(filename="inheritance.log", level=logging.INFO, format= '%(levelname)s %(asctime)s %(name)s %(message)s')


# inheritance
# multiple inheritance
# Example 1
class ineuron6:
    logging.info("This is a class called ineuron6")
    try:
        logging.info("Creating methods in the class inuron6")
        def ineuron_students(self):
            print("List out the details of all the ineuron students")
            logging.info("List out the details of all the ineuron students")
        def no_of_courses(self):
            print("List out all the courses offered by ineuron")
            logging.info("List out all the courses offered by ineuron")
        def job_guarantee_courses(self):
            print("List out the details of all the job guarantee courses offered by ineuron")
            logging.info("List out the details of all the job guarantee courses offered by ineuron")
    except Exception as e:
        logging.exception(e)
        print(e)

class ineuron_6:
    logging.info("This is a class called ineuron_6")
    try:
        logging.info("Creating methods in the class inuron_6")
        def student_login(self):
            print("List out all the student login details")
            logging.info("List out all the student login details")
        def ineuron_signup(self):
            print("List out all the details to be filled during signup")
            logging.info("List out all the student login details")
    except Exception as e:
        logging.exception(e)
        print(e)

class ineuron_6_:
    logging.info("This is a class called ineuron_6_")
    try:
        logging.info("Creating method in the ineuron_6_ class")
        def internship(self):
            print("List out all the internship field available")
            logging.info("List out all the internship field available")
    except Exception as e:
        logging.exception(e)
        print(e)

class i6(ineuron6, ineuron_6, ineuron_6_):
    logging.info("This is a class called i6")
    pass

six = i6()
six.ineuron_students()
six.no_of_courses()
six.job_guarantee_courses()
six.student_login()
six.ineuron_signup()
six.internship()
logging.info(six.ineuron_students())
logging.info(six.no_of_courses())
logging.info(six.job_guarantee_courses())
logging.info(six.student_login())
logging.info(six.ineuron_signup())
logging.info(six.internship())




# inheritance
# multiple inheritance
# Example 2
class student6:
    logging.info("This is a class called student6")
    try:
        logging.info("Creating methods in the class called student6")

        def student_name6(self):
            print("List out the names of all the students")
            logging.info("List out the names of all the students")

        def enrollment_no6(self):
            print("List out the enrollment numbers of all the students")
            logging.info("List out the enrollment numbers of all the students")

        def id_no6(self):
            print("List out the id numbers of all the students")
            logging.info("List out the id numbers of all the students")
    except Exception as e:
        logging.exception(e)
        print(e)


class student_6:
    logging.info("This is a class called student_6")
    try:
        logging.info("Creating methods in the class called student_6")

        def course_name6(self):
            print("List out the all course names taken by the student")
            logging.info("List out the all course names taken by the student")

        def course_duration6(self):
            print("List out the duration of each individual course")
            logging.info("List out the duration of each individual course")
    except Exception as e:
        logging.exception(e)
        print(e)


class student_6_(student6, student_6):
    logging.info("This is a class called student_6_")
    pass


s6 = student_6_()
s6.student_name6()
s6.enrollment_no6()
s6.id_no6()
s6.course_name6()
s6.course_duration6()
logging.info(s6.student_name6())
logging.info(s6.enrollment_no6())
logging.info(s6.id_no6())
logging.info(s6.course_name6())
logging.info(s6.course_duration6())



# inheritance
# multiple inheritance
# Example 3
class courses6:
    logging.info("This is a class called courses6")
    try:
        logging.info("Creating methods in the courses6 class")

        def course_name6(self):
            print("List out the name of all the courses offered")
            logging.info("List out the name of all the courses offered")

        def no_of_courses6(self):
            print("List out the number of courses offered")
            logging.info("List out the number of courses offered")
    except Exception as e:
        loggin.exception(e)
        print(e)


class courses_6:
    logging.info("This is another class called courses_6")
    try:
        logging.info("Creating methods in the course_6 class")

        def course_duration6(self):
            print("List out the course duration of each individual course")
            logging.info("List out the course duration of each individual course")

        def course_modules6(self):
            print("List out the number of modules in each course respectively")
            logging.info("List out the number of modules in each course respectively")
    except Exception as e:
        loggin.exception(e)
        print(e)


class courses_6_(courses6, courses_6):
    logging.info("This is another class called courses_6_")
    pass


c6 = courses_6_()
c6.course_name6()
c6.no_of_courses6()
c6.course_duration6()
c6.course_modules6()
logging.info(c6.course_name6())
logging.info(c6.no_of_courses6())
logging.info(c6.course_duration6())
logging.info(c6.course_modules6())



# inheritance
# multiple inheritance
# Example 4
class blogs6:
    logging.info("This is a class called blogs6")
    try:
        logging.info("Creating methods in the blogs6 class")

        def blog_title6(self):
            print("List out only the titles of the blogs on the website")
            logging.info("List out only the titles of the blogs on the website")

        def no_of_blogs6(self):
            print("List out the number of blogs based on the individual categories")
            logging.info("List out the number of blogs based on the individual categories")
    except Exception as e:
        logging.exception(e)
        print(e)


class blogs_6:
    logging.info("This is a class called blogs_6")
    try:
        logging.info("Creating methods inside the blogs_6 class")

        def blog_category6(self):
            print("List out the different categories")
            logging.info("List out the different categories")

        def archive6(self):
            print("List the archives on the website")
            logging.info("List the archives on the website")
    except Exception as e:
        logging.exception(e)
        print(e)


class blogs_6_(blogs6, blogs_6):
    logging.info("This is another class called blogs_6_")
    pass


b6 = blogs_6_()
b6.blog_title6()
b6.no_of_blogs6()
b6.blog_category6()
b6.archive6()
logging.info(b6.blog_title6())
logging.info(b6.no_of_blogs6())
logging.info(b6.blog_category6())
logging.info(b6.archive6())



# inheritance
# multiple inheritance
# Example 5
class internship6:
    logging.info("This is a class called internship6")
    try:
        logging.info("Creating methods in the internship6 class")

        def student_name6(self):
            print("List out the names of all the students that are in the internship program")
            logging.info("List out the names of all the students that are in the internship program")

        def student_id_no6(self):
            print("List out the id number of all the students")
            logging.info("List out the id number of all the students")
    except Exception as e:
        logging.exception(e)
        print(e)


class internship_6:
    logging.info("This is another class called internship_6")
    try:
        logging.info("Creating methods in the internship_6 class")

        def domain_name6(self):
            print("List all the names of the domains that are available for download")
            logging.info("List all the names of the domains that are available for download")

        def internship_duration(self):
            print("List out the duration of internship according to each individual domain")
            logging.info("List out the duration of internship according to each individual domain")
    except Exception as e:
        logging.exception(e)
        print(e)


class internship_6_(internship6, internship_6):
    logging.info("This is another class called internship_6_")
    pass


intern6 = internship_6_()
intern6.student_name6()
intern6.student_id_no6()
intern6.domain_name6()
intern6.internship_duration()
logging.info(intern6.student_name6())
logging.info(intern6.student_id_no6())
logging.info(intern6.domain_name6())
logging.info(intern6.internship_duration())




# inheritance
# multi-level inheritance
# Example 6
class ineuron5:
    logging.info("This is a class called ineuron5")
    try:
        logging.info("Creating methods inside the ineuron5 class")
        def courses(self):
            print("List out all the courses that are offered")
            logging.info("List out all the courses that are offered")
        def no_of_courses(self):
            print("List of the total number of courses available")
            logging.info("List out all the courses that are offered")
        def internship(self):
            print("List out all the fields of internship offered")
    except Exception as e:
        logging.exception(e)
        print(e)

class FSDS(ineuron5):
    logging.info("This is a class called FSDS")
    try:
        logging.info("Creating method inside the FSDS class")
        def no_of_modules(self):
            print("List all the modules that needs to be completed to finish the entire FSDS course")
            logging.info("List all the modules that needs to be completed to finish the entire FSDS course")
    except Exception as e:
        logging.exception(e)
        print(e)

class FSDS_student_portal(FSDS):
    logging.info("This is a class called FSDS_student_portal")
    pass

FSDS_sp = FSDS_student_portal()
FSDS_sp.courses()
FSDS_sp.no_of_courses()
FSDS_sp.internship()
FSDS_sp.no_of_modules()
logging.info(FSDS_sp.courses())
logging.info(FSDS_sp.no_of_courses())
logging.info(FSDS_sp.internship())
logging.info(FSDS_sp.no_of_modules())



# inheritance
# multi-level inheritance
# Example 7
class jobs5:
    logging.info("This is a class called jobs5")
    try:
        logging.info("Creating methods inside jobs5 class")

        def emp_name5(self):
            print("List out the names of all the employees")
            logging.info("List out the names of all the employees")

        def emp_id5(self):
            print("List of the id number of the all the employees")
            logging.info("List of the id number of the all the employees")
    except Exception as e:
        logging.exception(e)
        print(e)


class jobs_5(jobs5):
    logging.info("This is a class called jobs_5")
    try:
        logging.info("Creating methods inside the jobs_5 class")

        def emp_desigination5(self):
            print("List out the desigination of all the employees")
            logging.info("List out the desigination of all the employees")

        def emp_salary5(self):
            print("List out the salaries of all the employees")
            logging.info("List out the salaries of all the employees")
    except Exception as e:
        logging.exception(e)
        print(e)


class jobs_5_(jobs_5):
    logging.info("This is a class called jobs_5_")
    pass


j5 = jobs_5_()
j5.emp_name5()
j5.emp_id5()
j5.emp_desigination5()
j5.emp_salary5()
logging.info(j5.emp_name5())
logging.info(j5.emp_id5())
logging.info(j5.emp_desigination5())
logging.info(j5.emp_salary5())



# inheritance
# multi-level inheritance
# Example 8
class affilates5:
    logging.info("This is a class called affilates5")
    try:
        logging.info("Creating methods in the affilates5 class")

        def affilates_name(self):
            print("List out the name of all the affilates")
            logging.info("List out the name of all the affilates")

        def affilates_function(self):
            print("List out the function of each affilates")
            logging.info("List out the function of each affilates")
    except Exception as e:
        logging.exception(e)
        print(e)


class affilates_5(affilates5):
    logging.info("This is a class called affilates_5")
    try:
        logging.info("Creating methods in the affilates_5 class")

        def no_of_affilates5(self):
            print("List out the numbers of affilates")
            logging.info("List out the numbers of affilates")
    except Exception as e:
        logging.exception(e)
        print(e)


class affilates_5_(affilates_5):
    logging.info("This is a class called affilates_5_")
    pass


a5 = affilates_5_()
a5.affilates_name()
a5.affilates_function()
a5.no_of_affilates5()
logging.info(a5.affilates_name())
logging.info(a5.affilates_function())
logging.info(a5.no_of_affilates5())



# inheritance
# multi-level inheritance
# Example 9
class class_type5:
    logging.info("This is a class called class_type5")
    try:
        logging.info("Creating methods in the class_type5 class")

        def student_name5(self):
            print("List out the names of all the students")
            logging.info("List out the names of all the students")

        def course_name5(self):
            print("List out the name of all the courses")
            logging.info("List out the name of all the courses")
    except Exception as e:
        logging.exception(e)
        print(e)


class class_type_5(class_type5):
    logging.info("This is a class called class_type_5")
    try:
        logging.info("Creating methods in the class_type_5 class")

        def course_module5(self):
            print("List out the number of modules in each course")
            logging.info("List out the number of modules in each course")

        def course_duration5(self):
            print("List out the duration of each course")
            logging.info("List out the duration of each course")
    except Exception as e:
        logging.exception(e)
        print(e)


class class_type_5_(class_type_5):
    logging.info("This is a class called class_type_5")
    pass


ct5 = class_type_5_()
ct5.student_name5()
ct5.course_name5()
ct5.course_module5()
ct5.course_duration5()
logging.info(ct5.student_name5())
logging.info(ct5.course_name5())
logging.info(ct5.course_module5())
logging.info(ct5.course_duration5())



# inheritance
# multi-level inheritance
# Example 10
class hackathon5:
    logging.info("This is a class called hackathon5")
    try:
        logging.info("Creating methods in the hackathon5 class")

        def team_name5(self):
            print("List out the names of all the teams")
            logging.info("List out the names of all the teams")

        def no_of_team_members5(self):
            print("List out the number of team members in each team")
            logging.info("List out the number of team members in each team")
    except Exception as e:
        logging.exception(e)
        print(e)


class hackathon_5(hackathon5):
    logging.info("This is a class called hackathon_5")
    try:
        logging.info("Creating methods in the hackathon_5 class")

        def project_title5(self):
            print("List out the project titles")
            logging.info("List out the project titles")
    except Exception as e:
        logging.exception(e)
        print(e)


class hackathon_5_(hackathon_5):
    logging.info("This is a class called hackathon_5_")
    pass


hat5 = hackathon_5_()
hat5.team_name5()
hat5.no_of_team_members5()
hat5.project_title5()
logging.info(hat5.team_name5())
logging.info(hat5.no_of_team_members5())
logging.info(hat5.project_title5())