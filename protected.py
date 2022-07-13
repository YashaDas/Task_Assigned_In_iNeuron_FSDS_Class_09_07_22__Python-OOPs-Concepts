import logging
logging.basicConfig(filename="protected.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')


# Example 1
class ineuron2:
    logging.info("This is a class called ineuron2")
    try:
        def __init__(self, student_name2, no_of_courses2):
            logging.info("Creating protected variables inside the constructor for ineuron2 class")
            self._student_name2 = student_name2
            self._no_of_courses2 = no_of_courses2
    except Exception as e:
        logging.exception(e)
        print(e)


iv2 = ineuron2("John Waters", 2)
print(iv2._student_name2)
print(iv2._no_of_courses2)
logging.info(iv2._student_name2)
logging.info(iv2._no_of_courses2)

# Example 2
class student2:
    logging.info("This is a class called student2")
    try:
        def __init__(self, student_name2, enrollment_no2, id_no2):
            logging.info("Creating protected variables inside the constructor for student2 class")
            self._student_name2 = student_name2
            self._enrollment_no2 = enrollment_no2
            self._id_no2 = id_no2
    except Exception as e:
        loggin.exception(e)
        print(e)


s2 = student2("Zoey", 109876, 204)
print(s2._student_name2)
print(s2._enrollment_no2)
print(s2._id_no2)
logging.info(s2._student_name2)
logging.info(s2._enrollment_no2)
logging.info(s2._id_no2)


# Example 3
class courses2:
    logging.info("This is a class called courses2")
    try:
        def __init__(self, course_name2, no_of_courses2):
            logging.info("Creating protected variables inside the constructor for courses2 class")
            self._course_name2 = course_name2
            self._no_of_courses2 = no_of_courses2
    except Exception as e:
        loggin.exception(e)
        print(e)


c2 = courses2("Big Data", 4)
print(c2._course_name2)
print(c2._no_of_courses2)
logging.info(c2._course_name2)
logging.info(c2._no_of_courses2)

# Example 4
class blogs2:
    logging.info("This is a class called blogs2")
    try:
        def __init__(self, blog_title2, no_of_blogs2):
            logging.info("Creating protected variables inside the constructor for blogs2 class")
            self._blog_title2 = blog_title2
            self._no_of_blogs2 = no_of_blogs2
    except Exception as e:
        logging.exception(e)
        print(e)


b2 = blogs2("Blog title 2", 7)
print(b2._blog_title2)
print(b2._no_of_blogs2)
logging.info(b2._blog_title2)
logging.info(b2._no_of_blogs2)


# Example 5
class internship2:
    logging.info("This is a class called internship2")
    try:
        def __init__(self, student_name2, student_id_no2, course_name2, internship_duration2):
            logging.info("Creating protected variables inside the constructor for internship2 class")
            self._student_name2 = student_name2
            self._student_id_no2 = student_id_no2
            self._course_name2 = course_name2
            self._internship_duration2 = internship_duration2
    except Exception as e:
        logging.exception(e)
        print(e)


intern2 = internship2("Violet", 409, "Physics", "4 months")
print(intern2._student_name2)
print(intern2._student_id_no2)
print(intern2._course_name2)
print(intern2._internship_duration2)
logging.info(intern2._student_name2)
logging.info(intern2._student_id_no2)
logging.info(intern2._course_name2)
logging.info(intern2._internship_duration2)


# Example 6
class jobs2:
    logging.info("This is a class called jobs2")
    try:
        def __init__(self, emp_name2, emp_id2, emp_salary2):
            logging.info("Creating protected variables inside the constructor for jobs2 class")
            self._emp_name2 = emp_name2
            self._emp_id2 = emp_id2
            self._emp_salary2 = emp_salary2
    except Exception as e:
        logging.exception(e)
        print(e)

j2 = jobs2("Erica", 509, 45000)
print(j2._emp_name2)
print(j2._emp_id2)
print(j2._emp_salary2)
logging.info(j2._emp_name2)
logging.info(j2._emp_id2)
logging.info(j2._emp_salary2)


# Example 7
class affilates2:
    logging.info("This is a class called affilates2")
    try:
        def __init__(self, affiltates_name2, no_of_affilates2):
            logging.info("Creating protected variables inside the constructor for affilates2 class")
            self._affilates_name2 = affiltates_name2
            self._no_of_affilates2 = no_of_affilates2
    except Exception as e:
        logging.exception(e)
        print(e)


a2 = affilates2("XYZ Digitals", 6)
print(a2._affilates_name2)
print(a2._no_of_affilates2)
logging.info(a2._affilates_name2)
logging.info(a2._no_of_affilates2)


# Example 8
class class_type2:
    logging.info("This is a class called class_type2")
    try:
        def __init__(self, student_name2, course_name2):
            logging.info("Creating protected variables inside the constructor for class_type2 class")
            self._student_name2 = student_name2
            self._course_name2 = course_name2
    except Exception as e:
        logging.exception(e)
        print(e)


ct2 = class_type2("Hari", "Science")
print(ct2._student_name2)
print(ct2._course_name2)
logging.info(ct2._student_name2)
logging.info(ct2._course_name2)


# Example 9
class student_portal2:
    logging.info("This is a class called student_portal2")
    try:
        def __init__ (self, student_id2, student_password2):
            logging.info("Creating protected variables inside the constructor for student_portal1 class")
            self._student_id2 = student_id2
            self._student_password2 = student_password2
    except Exception as e:
        logging.exception(e)
        print(e)

sp2 = student_portal2(2067, "xyz@123")
print(sp2._student_id2)
print(sp2._student_password2)
logging.info(sp2._student_id2)
logging.info(sp2._student_password2)


# Example 10
class hackathon2:
    logging.info("This is a class called hackathon2")
    try:
        def __init__(self, team_name2, no_of_team_members2, project_title2):
            logging.info("Creating protected variables inside the constructor for hackathon2 class")
            self._team_name2 = team_name2
            self._no_of_team_members2 = no_of_team_members2
            self._project_title2 = project_title2
    except Exception as e:
        logging.exception(e)
        print(e)


hat2 = hackathon2("Coders", 7, "This is a project title 2")
print(hat2._team_name2)
print(hat2._no_of_team_members2)
print(hat2._project_title2)
logging.info(hat2._team_name2)
logging.info(hat2._no_of_team_members2)
logging.info(hat2._project_title2)