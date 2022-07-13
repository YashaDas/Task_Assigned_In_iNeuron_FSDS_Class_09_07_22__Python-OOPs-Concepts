import logging
logging.basicConfig(filename="ploymorphism.log", level=logging.INFO, format= '%(levelname)s %(asctime)s %(name)s %(message)s')


# Example 1
class ineuron4:
    logging.info("This is a class called ineuron4")
    try:
        logging.info("Creating a method inside the ineuron4 class called student_1")
        def student_1(self):
            print("List out the details of all the students")
            logging.info("List out the details of all the students")
    except Exception as e:
        logging.exception(e)
        print(e)

class ineuron_4:
    logging.info("This is another class called ineuron_4")
    try:
        logging.info("Creating a method inside the ineuron_4 class called student_1")
        def student_1(self):
            print("List the details of only those students that are enrolled in the FSDS class")
            logging.info("List the details of only those students that are enrolled in the FSDS class")
    except Exception as e:
        logging.exception(e)
        print(e)

def ineuron_exetrnal(a):
    try:
        logging.info("This an external method called ineuron_external")
        a.student_1()
    except Exception as e:
        logging.exception(e)
        print(e)

iv4 = ineuron4()
iv_4 = ineuron_4()
ineuron_exetrnal(iv4)
ineuron_exetrnal(iv_4)
logging.info(ineuron_exetrnal(iv4))
logging.info(ineuron_exetrnal(iv_4))



# Example 2
class student4:
    logging.info("This is a class called student4")
    try:
        logging.info("Creating a method inside the student4 class called idno_4")
        def id_no4(self):
            print("List out the id number of all the students")
            logging.info("List out the id number of all the students")
    except Exception as e:
        logging.info(e)
        print(e)
class student_4:
    logging.info("This is another class called student_4")
    try:
        logging.info("Creating a method inside the student_4 class called id_no4")
        def id_no4(self):
            print("List out the id number of only those students whose id number ends with 3")
            logging.info("List out the id number of only those students whose id number ends with 3")
    except Exception as e:
        logging.exception(e)
        print(e)

def student_external(a):
    try:
        logging.info("This an external method called student_external")
        a.id_no4()
    except Exception as e:
        logging.exception(e)
        print(e)

s4 = student4()
s_4 = student_4()
student_external(s4)
student_external(s_4)
logging.info(student_external(s4))
logging.info(student_external(s_4))



# Example 3
class courses4:
    logging.info("This is a class called courses4")
    try:
        logging.info("Creating a method inside the courses4 class called course_name4")

        def course_name4(self):
            print("List out all the names of the courses offered")
            logging.info("List out all the names of the courses offered")
    except Exception as e:
        loggin.exception(e)
        print(e)


class courses_4:
    logging.info("This is another class called courses_4")
    try:
        logging.info("Creating a method inside the courses_4 class called course_name4")

        def course_name4(self):
            print("List the names that are being offered in this semester only")
            logging.info("List the names that are being offered in this semester only")
    except Exception as e:
        loggin.exception(e)
        print(e)


def courses_external(a):
    try:
        logging.info("This an external method called courses_external")
        a.course_name4()
    except Exception as e:
        loggin.exception(e)
        print(e)


c4 = courses4()
c_4 = courses_4()
courses_external(c4)
courses_external(c_4)
logging.info(courses_external(c4))
logging.info(courses_external(c_4))



# Example 4
class blogs4:
    logging.info("This is a class called blogs4")
    try:
        logging.info("Creating a method inside the blogs4 class called blog_title4")

        def blog_title4(self):
            print("List out all the blogs available on the website")
            logging.info("List out all the blogs available on the website")
    except Exception as e:
        logging.exception(e)
        print(e)


class blogs_4:
    logging.info("This is another class called blogs_4")
    try:
        logging.info("Creating a method inside the blogs_4 class called blog_title4")

        def blog_title4(self):
            print("List out only the blogs related to Data Science")
            logging.info("List out only the blogs related to Data Science")
    except Exception as e:
        logging.exception(e)
        print(e)


def blogs_external(a):
    try:
        logging.info("This an external method called blogs_external")
        a.blog_title4()
    except Exception as e:
        loggin.exception(e)
        print(e)


b4 = blogs4()
b_4 = blogs_4()
blogs_external(b4)
blogs_external(b_4)
logging.info(blogs_external(b4))
logging.info(blogs_external(b_4))



# Example 5
class internship4:
    logging.info("This is a class called internship4")
    try:
        logging.info("Creating a method inside the internship4 class called student_name4")
        def student_name4(self):
            print("List out the name of all the students")
            logging.info("List out the name of all the students")
    except Exception as e:
        logging.exception(e)
        print(e)

class internship_4:
    logging.info("This is another class called internship_4")
    try:
        logging.info("Creating a method inside the internship_4 class called student_name4")
        def student_name4(self):
            print("List out only the name of students that are eligible for internship")
            logging.info("List out only the name of students that are eligible for internship")
    except Exception as e:
        logging.exception(e)
        print(e)

def internship_external(a):
    try:
        logging.info("This an external method called internship_external")
        a.student_name4()
    except Exception as e:
        logging.exception(e)
        print(e)


intern4 = internship4()
intern_4 = internship_4()
internship_external(intern4)
internship_external(intern_4)
logging.info(internship_external(intern4))
logging.info(internship_external(intern_4))



# Example 6
class jobs4:
    logging.info("This is class called jobs4")
    try:
        logging.info("Creating a method inside the jobs4 class called emp_salary4")

        def emp_salary4(self):
            print("List out the salary of all the employees")
            logging.info("List out the salary of all the employees")
    except Exception as e:
        logging.exception(e)
        print(e)


class jobs_4:
    logging.info("This is another class called jobs_4")
    try:
        logging.info("Creating a method inside the jobs_4 class called emp_salary4")

        def emp_salary4(self):
            print("List out the salaries of only the employees working in the data department")
            logging.info("List out the salaries of only the employees working in the data department")
    except Exception as e:
        logging.exception(e)
        print(e)


def jobs_external(a):
    try:
        logging.info("This an external method called jobs_external")
        a.emp_salary4()
    except Exception as e:
        logging.exception(e)
        print(e)


j4 = jobs4()
j_4 = jobs_4()
jobs_external(j4)
jobs_external(j_4)
logging.info(jobs_external(j4))
logging.info(jobs_external(j_4))



# Example 7
class affilates4:
    logging.info("This is a class called affilates4")
    try:
        logging.info("Creating a method inside the affilates4 class called affilates_name4")

        def affilates_name4(self):
            print("List out the name of all the affilates")
            logging.info("List out the name of all the affilates")
    except Exception as e:
        logging.info(e)
        print(e)


class affilates_4:
    logging.info("This is another class called affilates_4")
    try:
        logging.info("Creating a method inside the affilates_4 class called affilates_name4")

        def affilates_name4(self):
            print("List out the name of affilates that are related to finance sector")
            logging.info("List out the name of affilates that are related to finance sector")
    except Exception as e:
        logging.info(e)
        print(e)


def affilates_external(a):
    try:
        logging.info("This an external method called affilates_external")
        a.affilates_name4()
    except Exception as e:
        logging.info(e)
        print(e)


a4 = affilates4()
a_4 = affilates_4()
affilates_external(a4)
affilates_external(a_4)
logging.info(affilates_external(a4))
logging.info(affilates_external(a_4))



# Example 8
class class_type4:
    logging.info("This is a class called class_type4")
    try:
        logging.info("Creating a method inside the class_type4 class called course_name4")

        def course_name4(self):
            print("List out the names of all the courses offered")
            logging.info("List out the names of all the courses offered")
    except Exception as e:
        logging.exception(e)
        print(e)


class class_type_4:
    logging.info("This is another class called class_type_4")
    try:
        logging.info("Creating a method inside the class_type_4 called course_name4")

        def course_name4(self):
            print("List out only the name of courses that are being offered this semester")
            logging.info("List out only the name of courses that are being offered this semester")
    except Exception as e:
        logging.exception(e)
        print(e)


def class_type_external(a):
    try:
        logging.info("This an external method called affilates_external")
        a.course_name4()
    except Exception as e:
        logging.exception(e)
        print(e)


ct4 = class_type4()
ct_4 = class_type_4()
class_type_external(ct4)
class_type_external(ct_4)
logging.info(class_type_external(ct4))
logging.info(class_type_external(ct_4))



# Example 9
class student_portal4:
    logging.info("This is a class called student_portal4")
    try:
        logging.info("Creating a method inside the student_portal4 class called student_id4")

        def student_id4(self):
            print("List out the id number of all the students")
            logging.info("List out the id number of all the students")
    except Exception as e:
        logging.exception(e)
        print(e)


class student_portal_4:
    logging.info("This is another class called student_portal_4")
    try:
        logging.info("Creating a method inside the student_portal_4 class called student_id4")

        def student_id4(self):
            print("List out the id number of only those students that have registered for this session")
            logging.info("List out the id number of only those students that have registered for this session")
    except Exception as e:
        logging.exception(e)
        print(e)


def student_portal_external(a):
    try:
        logging.info("This an external method called affilates_external")
        a.student_id4()
    except Exception as e:
        logging.exception(e)
        print(e)


sp4 = student_portal4()
sp_4 = student_portal_4()
student_portal_external(sp4)
student_portal_external(sp_4)
logging.info(student_portal_external(sp4))
logging.info(student_portal_external(sp_4))



# Example 10
class hackathon4:
    logging.info("This is a class called hackathon4")
    try:
        logging.info("Creating a method inside the hackathon4 class called no_of_team_members4")

        def no_of_team_members4(self):
            print("List out the total number of team members")
            logging.info("List out the total number of team members")
    except Exception as e:
        logging.exception(e)
        print(e)


class hackathon_4:
    logging.info("This is another class called hackathon_4")
    try:
        logging.info("Creating a method inside the hackathon_4 class called no_of_team_members4")

        def no_of_team_members4(self):
            print("List out the number of team memebers in each team")
            logging.info("List out the number of team memebers in each team")
    except Exception as e:
        logging.exception(e)
        print(e)


def hackathon_external(a):
    try:
        logging.info("This is an external method called hackathon_external")
        a.no_of_team_members4()
    except Exception as e:
        logging.exception(e)
        print(e)


hat4 = hackathon4()
hat_4 = hackathon_4()
hackathon_external(hat4)
hackathon_external(hat_4)
logging.info(hackathon_external(hat4))
logging.info(hackathon_external(hat_4))