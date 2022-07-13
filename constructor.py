import logging

logging.basicConfig(filename="constructor.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

# Example 1
class ineuron:
  logging.info("This is a class called ineuron")
  try:
    logging.info("Creating a constructor for the ineuron class")

    def __init__(self, student_name, no_of_courses):
      logging.info("Creating the variables inside the constructor for ineuron class")
      self.student_name = student_name
      self.no_of_courses = no_of_courses
  except Exception as e:
    loggin.exception(e)
    print(e)


iv = ineuron("Yasha Das", 3)
print(iv.student_name, iv.no_of_courses)
logging.info(iv.student_name)
logging.info(iv.no_of_courses)


# Example 2
class student:
    logging.info("This is a class called student")
    try:
        logging.info("Creating a constructor for the student class")
        def __init__(self, student_name, enrollment_no, id_no):
            logging.info("Creating the variables inside the constructor for student class")
            self.student_name = student_name
            self.enrollment_no = enrollment_no
            self.id_no = id_no
    except Exception as e:
        loggin.exception(e)
        print(e)

s = student("XYZABC", 1122334455, 1035)
print(s.student_name, s.enrollment_no, s.id_no)
logging.info(s.student_name)
logging.info(s.enrollment_no)
logging.info(s.id_no)


# Example 3
class courses:
  logging.info("This is a class called courses")
  try:
    logging.info("Creating a constructor for the courses class")

    def __init__(self, course_name, no_of_courses):
      logging.info("Creating the variables inside the constructor for courses class")
      self.course_name = course_name
      self.no_of_courses = no_of_courses
  except Exception as e:
    loggin.exception(e)
    print(e)


c = courses("Full Stack Data Science", 3)
print(c.course_name, c.no_of_courses)
logging.info(c.course_name)
logging.info(c.no_of_courses)


# Example 4
class blogs:
    logging.info("This is a class called blogs")
    try:
        logging.info("Creating a constructor for the blogs class")
        def __init__(self, blog_title, no_of_blogs):
            logging.info("Creating the variables inside the constructor for blogs class")
            self.blog_title = blog_title
            self.no_of_blogs = no_of_blogs
    except Exception as e:
        logging.exception(e)
        print(e)

b = blogs("Introduction to Basic Python", 1)
print(b.blog_title, b.no_of_blogs)
logging.info(b.blog_title)
logging.info(b.no_of_blogs)


# Example 5
class internship:
  logging.info("This is a class called internship")
  try:
    logging.info("Creating a constructor for the internship class")

    def __init__(self, student_name, student_id_no, course_name, internship_duration):
      logging.info("Creating the variables inside the constructor for internship class")
      self.student_name = student_name
      self.student_id_no = student_id_no
      self.course_name = course_name
      self.internship_duration = internship_duration
  except Exception as e:
    logging.exception(e)
    print(e)


intern = internship("XYZABC", 1053, "Full Stack Data Science", "6 months")
print(intern.student_name, intern.student_id_no, intern.course_name, intern.internship_duration)
logging.info(intern.student_name)
logging.info(intern.student_id_no)
logging.info(intern.course_name)
logging.info(intern.internship_duration)


# Example 6
class jobs:
  logging.info("This is a class called jobs")
  try:
    logging.info("Creating a constructor for the jobs class")

    def __init__(self, emp_name, emp_id, emp_salary):
      logging.info("Creating the variables inside the constructor for jobs class")
      self.emp_name = emp_name
      self.emp_id = emp_id
      self.emp_salary = emp_salary
  except Exception as e:
    logging.exception(e)
    print(e)


j = jobs("QWERTY", 2201, 45000)
print(j.emp_name, j.emp_id, j.emp_salary)
logging.info(j.emp_name)
logging.info(j.emp_id)
logging.info(j.emp_salary)


# Example 7
class affilates:
  logging.info("This is a class called affilates")
  try:
    logging.info("Creating a constructor for the affilates class")

    def __init__(self, affiltates_name, no_of_affilates):
      logging.info("Creating the variables inside the constructor for affilates class")
      self.affilates_name = affiltates_name
      self.no_of_affilates = no_of_affilates
  except Exception as e:
    logging.exception(e)
    print(e)


a = affilates("ADBC", 1)
print(a.affilates_name, a.no_of_affilates)
logging.info(a.affilates_name)
logging.info(a.no_of_affilates)


# Example 8
class class_type:
  logging.info("This is a class called class_type")
  try:
    logging.info("Creating a constructor for the class_type class")

    def __init__(self, student_name, course_name):
      logging.info("Creating the variables inside the constructor for class_type class")
      self.student_name = student_name
      self.course_name = course_name
  except Exception as e:
    logging.exception(e)
    print(e)


ct = class_type("Qwerty poiuy", "FSDS")
print(ct.student_name, ct.course_name)
logging.info(ct.student_name)
logging.info(ct.course_name)


# Example 9
class student_portal:
  logging.info("This is a class called student_portal")
  try:
    logging.info("Creating a constructor for the student_portal class")

    def __init__(self, student_id, student_password):
      logging.info("Creating the variables inside the constructor for student_portal class")
      self.student_id = student_id
      self.student_password = student_password
  except Exception as e:
    logging.exception(e)
    print(e)


sp = student_portal(1001, "timeline@123")
print(sp.student_id, sp.student_password)
logging.info(sp.student_id)
logging.info(sp.student_password)


# Example 10
class hackathon:
  logging.info("This is a class called hackathon")
  try:
    logging.info("Creating a constructor for the hackathon class")

    def __init__(self, team_name, no_of_team_members, project_title):
      logging.info("Creating the variables inside the constructor for hackathon class")
      self.team_name = team_name
      self.no_of_team_members = no_of_team_members
      self.project_title = project_title
  except Exception as e:
    logging.exception(e)
    print(e)


hat = hackathon("Error_Free", 5, "Virtual Health Assistant")
print(hat.team_name, hat.no_of_team_members, hat.project_title)
logging.info(hat.team_name)
logging.info(hat.no_of_team_members)
logging.info(hat.project_title)