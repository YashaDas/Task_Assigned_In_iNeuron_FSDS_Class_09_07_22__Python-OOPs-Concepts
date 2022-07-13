import logging
logging.basicConfig(filename="private.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')


#Example 1
class ineuron1:
    logging.info("This is a class called ineuron1")
    try:
        def __init__(self, student_name1, no_of_courses1):
            logging.info("Creating private variables inside the constructor for ineuron1 class")
            self.__student_name1 = student_name1
            self.__no_of_courses1 = no_of_courses1
    except Exception as e:
        logging.exception(e)
        print(e)


iv1 = ineuron1("Alice Wonderland", 1)
print(iv1._ineuron1__student_name1)
print(iv1._ineuron1__no_of_courses1)
logging.info(iv1._ineuron1__student_name1)
logging.info(iv1._ineuron1__no_of_courses1)


# Example 2
class student1:
    logging.info("This is a class called student1")
    try:
        def __init__(self, stud_name1, enrollment_no1, id_no1):
            logging.info("Creating private variables inside the constructor for student1 class")
            self.__stud_name1 = stud_name1
            self.__enrollment_no1 = enrollment_no1
            self.__id_no1 = id_no1
    except Exception as e:
        logging.exception(e)
        print(e)

s1 = student1("Bella", 12345, 102)
print(s1._student1__stud_name1)
print(s1._student1__enrollment_no1)
print(s1._student1__id_no1)
logging.info(s1._student1__stud_name1)
logging.info(s1._student1__enrollment_no1)
logging.info(s1._student1__id_no1)


# Example 3
class courses1:
    logging.info("This is a class called courses1")
    try:
         def __init__(self, course_name1, no_of_courses1):
            logging.info("Creating private variables inside the constructor for courses1 class")
            self.__course_name1 = course_name1
            self.__no_of_courses1 = no_of_courses1
    except Exception as e:
        loggin.exception(e)
        print(e)

c1 = courses1("Data Science", 1)
print(c1._courses1__course_name1)
print(c1._courses1__no_of_courses1)
logging.info(c1._courses1__course_name1)
logging.info(c1._courses1__no_of_courses1)


# Example 4
class blogs1:
    logging.info("This is a class called blogs1")
    try:
        def __init__(self, blog_title1, no_of_blogs1):
            logging.info("Creating private variables inside the constructor for blogs1 class")
            self.__blog_title1 = blog_title1
            self.__no_of_blogs1 = no_of_blogs1
    except Exception as e:
        logging.exception(e)
        print(e)


b1 = blogs1("This is a blog title", 2)
print(b1._blogs1__blog_title1)
print(b1._blogs1__no_of_blogs1)
logging.info(b1._blogs1__blog_title1)
logging.info(b1._blogs1__no_of_blogs1)

# Example 5
class internship1:
    logging.info("This is a class called internship1")
    try:
        def __init__(self, student_name1, student_id_no1, course_name1, internship_duration1):
            logging.info("Creating private variables inside the constructor for internship1 class")
            self.__student_name1 = student_name1
            self.__student_id_no1 = student_id_no1
            self.__course_name1 = course_name1
            self.__internship_duration1 = internship_duration1
    except Exception as e:
        logging.exception(e)
        print(e)


intern1 = internship1("AlpaBeta", 103, "Blockchain", "6 months")
print(intern1._internship1__student_name1)
print(intern1._internship1__student_id_no1)
print(intern1._internship1__course_name1)
print(intern1._internship1__internship_duration1)
logging.info(intern1._internship1__student_name1)
logging.info(intern1._internship1__student_id_no1)
logging.info(intern1._internship1__course_name1)
logging.info(intern1._internship1__internship_duration1)

# Example 6
class jobs1:
    logging.info("This is a class called jobs1")
    try:
        def __init__(self, emp_name1, emp_id1, emp_salary1):
            logging.info("Creating private variables inside the constructor for jobs1 class")
            self.__emp_name1 = emp_name1
            self.__emp_id1 = emp_id1
            self.__emp_salary1 = emp_salary1
    except Exception as e:
        logging.exception(e)
        print(e)


j1 = jobs1("Jimmy Xyz", 1009, 30000)
print(j1._jobs1__emp_name1)
print(j1._jobs1__emp_id1)
print(j1._jobs1__emp_salary1)
logging.info(j1._jobs1__emp_name1)
logging.info(j1._jobs1__emp_id1)
logging.info(j1._jobs1__emp_salary1)

# Example 7
class affilates1:
    logging.info("This is a class called affilates1")
    try:
        def __init__(self, affiltates_name1, no_of_affilates1):
            logging.info("Creating private variables inside the constructor for affilates1 class")
            self.__affilates_name1 = affiltates_name1
            self.__no_of_affilates1 = no_of_affilates1
    except Exception as e:
        logging.exception(e)
        print(e)


a1 = affilates1("ABC Vision", 1)
print(a1._affilates1__affilates_name1)
print(a1._affilates1__no_of_affilates1)
logging.info(a1._affilates1__affilates_name1)
logging.info(a1._affilates1__no_of_affilates1)


# Example 8
class class_type1:
    logging.info("This is a class called class_type1")
    try:
        def __init__ (self, student_name1, course_name1):
            logging.info("Creating private variables inside the constructor for class_type1 class")
            self.__student_name1 = student_name1
            self.__course_name1 = course_name1
    except Exception as e:
        logging.exception(e)
        print(e)

ct1 = class_type1("sun moon", "Geography")
print(ct1._class_type1__student_name1)
print(ct1._class_type1__course_name1)
logging.info(ct1._class_type1__student_name1)
logging.info(ct1._class_type1__course_name1)


# Example 9
class student_portal1:
    logging.info("This is a class called student_portal1")
    try:
        logging.info("Creating a constructor for the student_portal class")
        def __init__ (self, student_id1, student_password1):
            logging.info("Creating private variables inside the constructor for student_portal1 class")
            self.__student_id1 = student_id1
            self.__student_password1 = student_password1
    except Exception as e:
        logging.exception(e)
        print(e)

sp1 = student_portal1(1004, "password123")
print(sp1._student_portal1__student_id1)
print(sp1._student_portal1__student_password1)
logging.info(sp1._student_portal1__student_id1)
logging.info(sp1._student_portal1__student_password1)


# Example 10
class hackathon1:
    logging.info("This is a class called hackathon1")
    try:
        def __init__ (self, team_name1, no_of_team_members1, project_title1):
            logging.info("Creating private variables inside the constructor for hackathon1 class")
            self.__team_name1 = team_name1
            self.__no_of_team_members1 = no_of_team_members1
            self.__project_title1 = project_title1
    except Exception as e:
        logging.exception(e)
        print(e)

hat1 = hackathon1("Dashers", 5, "This is a project title")
print(hat1._hackathon1__team_name1)
print(hat1._hackathon1__no_of_team_members1)
print(hat1._hackathon1__project_title1)
logging.info(hat1._hackathon1__team_name1)
logging.info(hat1._hackathon1__no_of_team_members1)
logging.info(hat1._hackathon1__project_title1)