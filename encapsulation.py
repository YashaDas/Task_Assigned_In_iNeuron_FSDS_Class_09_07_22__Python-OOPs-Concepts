import logging
logging.basicConfig(filename="encapsulation.log", level=logging.INFO, format= '%(levelname)s %(asctime)s %(name)s %(message)s')


# Example 1
class ineuron8:
    logging.info("This is a class called ineuron8")
    try:
        def __init__(self):
            self.__course = "Full Stack Data Science"

        def courses(self):
            print(self.__course)
            logging.info(self.__course)

        def change_course(self):
            self.__course = "Full Stack Data Analyst"
    except Exception as e:
        logging.exception(e)
        print(e)

iv8 = ineuron8()
iv8.courses()
iv8.change_course()
logging.info(iv8.courses())
logging.info(iv8.change_course())



# Example 2
class student8:
    logging.info("This is a class called student8")
    try:
        def __init__(self):
            self.__id_no8 = 1005

        def id_no8(self):
            print(self.__id_no8)
            logging.info(self.__id_no8)

        def change_id_no8(self):
            self.__id_no8 = 1009
    except Exception as e:
        logging.info(e)
        print(e)


s8 = student8()
s8.id_no8()
s8.change_id_no8()
logging.info(s8.id_no8())
logging.info(s8.change_id_no8())


# Example 3
class courses8:
    logging.info("This is a class called courses8")
    try:
        def __init__(self):
            self.__course_name8 = "Big Data"

        def course_name8(self):
            print(self.__course_name8)
            logging.info(self.__course_name8)

        def change_course_name8(self):
            self.__course_name8 = "IoT"
    except Exception as e:
        loggin.exception(e)
        print(e)


c8 = courses8()
c8.course_name8()
c8.change_course_name8()
logging.info(c8.course_name8())
logging.info(c8.change_course_name8())



# Example 4
class blogs8:
    logging.info("This is a class called blogs8")
    try:
        def __init__(self):
            self.__blog_title8 = "The title of the blog needs to be changed"

        def blog_title8(self):
            print(self.__blog_title8)
            logging.info(self.__blog_title8)

        def change_blog_title8(self):
            self.__blog_title8 = "The title of the blog is now changed"
    except Exception as e:
        logging.exception(e)
        print(e)


b8 = blogs8()
b8.blog_title8()
b8.change_blog_title8()
logging.info(b8.blog_title8())
logging.info(b8.change_blog_title8())



# Example 5
class internship8:
    logging.info("This is a class called internship8")
    try:
        def __init__(self):
            self.__student_name8 = "Harry"

        def student_name8(self):
            print(self.__student_name8)
            logging.info(self.__student_name8)

        def change_student_name8(self):
            self.__student_name8 = "Hari"
    except Exception as e:
        logging.exception(e)
        print(e)


intern8 = internship8()
intern8.student_name8()
intern8.change_student_name8()
logging.info(intern8.student_name8())
logging.info(intern8.change_student_name8())



# Example 6
class jobs8:
    logging.info("This is a class called jobs8")
    try:
        def __init__(self):
            self.__emp_salary8 = 7600

        def emp_salary8(self):
            print(self.__emp_salary8)
            logging.info(self.__emp_salary8)

        def change_emp_salary8(self):
            self.__emp_salary8 = 76000
    except Exception as e:
        logging.exception(e)
        print(e)


j8 = jobs8()
j8.emp_salary8()
j8.change_emp_salary8()
logging.info(j8.emp_salary8())
logging.info(j8.change_emp_salary8())



# Example 7
class affilates8:
    logging.info("This is a class called affilates8")
    try:
        def __init__(self):
            self.__affilates_name8 = "Green Valley Limited"

        def affilates_name8(self):
            print(self.__affilates_name8)
            logging.info(self.__affilates_name8)

        def change_affilates_name8(self):
            self.__affilates_name8 = "Green World Limited"
    except Exception as e:
        logging.info(e)
        print(e)


a8 = affilates8()
a8.affilates_name8()
a8.change_affilates_name8()
logging.info(a8.affilates_name8())
logging.info(a8.change_affilates_name8())



# Example 8
class class_type8:
    logging.info("This is a class called class_type8")
    try:
        def __init__(self):
            self.__course_name8 = "Data Structures"

        def course_name8(self):
            print(self.__course_name8)
            logging.info(self.__course_name8)

        def change_course_name8(self):
            self.__course_name8 = "OOPs Concept"
    except Exception as e:
        logging.exception(e)
        print(e)


ct8 = class_type8()
ct8.course_name8()
ct8.change_course_name8()
logging.info(ct8.course_name8())
logging.info(ct8.change_course_name8())



# Example 9
class student_portal8:
    logging.info("This is a class called student_portal8")
    try:
        def __init__(self):
            self.__student_id8 = 12345

        def student_id8(self):
            print(self.__student_id8)
            logging.info(self.__student_id8)

        def change_student_id8(self):
            self.__student_id8 = 90876
    except Exception as e:
        logging.exception(e)
        print(e)


sp8 = student_portal8()
sp8.student_id8()
sp8.change_student_id8()
logging.info(sp8.student_id8())
logging.info(sp8.change_student_id8())



# Example 10
class hackathon8:
    logging.info("This is a class called hackathon8")
    try:
        def __init__(self):
            self.__no_of_team_members8 = 5

        def no_of_team_members8(self):
            print(self.__no_of_team_members8)
            logging.info(self.__no_of_team_members8)

        def change_no_of_team_members8(self):
            self.__no_of_team_members8 = 7
    except Exception as e:
        logging.exception(e)
        print(e)


hat8 = hackathon8()
hat8.no_of_team_members8()
hat8.change_no_of_team_members8()
logging.info(hat8.no_of_team_members8())
logging.info(hat8.change_no_of_team_members8())