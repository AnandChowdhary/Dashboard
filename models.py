from django.db import models    # importing database library from Django   

class Members(models.Model):    # table for members' info

    CLASSES = (                 # tuples to store choices for each field
        (9, ’9’),               # (actual value to be stored, human-readable value),
        (10, ’10’),
        (11, ’11’),
        (12, ’12’),
    )

    DESIGNATIONS = (
        ('Mem', 'Member'),      
        ('ExecMem', 'Executive Member'),
        ('VicePres', 'Vice President'),
        ('Pres', 'President'),
    )

    DEPARTMENTS = (
        ('Quiz', 'Quizzing'),
        ('Design', 'Design'),
        ('Elec', 'Electronics'),
        ('Prog', 'Programming'),
    )
    
    sNo = models.IntegerField       # each statement represents a database column
    firstName = models.CharField('First Name', max_length = 20)
    lastName = models.CharField('Last Name', max_length = 20)
    schoolClass = models.IntegerField('Class', choices = CLASSES)
    desig = models.CharField('Designation', max_length = 20, choices = DESIGNATIONS)
    dept1 = models.CharField('Department 1', max_length = 20, choices = DEPARTMENTS)
    dept2 = models.CharField('Department 2', max_length = 20, choices = DEPARTMENTS)
    email = models.EmailField('Email ID')
    passwd = models.CharField('Password', max_length = 20)

class DepInfo(models.Model):        # table for info specific to each department

    DEPARTMENTS = (
        ('Quiz', 'Quizzing'),
        ('Design', 'Design'),
        ('Elec', 'Electronics'),
        ('Prog', 'Programming'),
    )

    dept1 = models.CharField('Department 1', max_length = 20, choices = DEPARTMENTS)
    dept2 = models.CharField('Department 2', max_length = 20, choices = DEPARTMENTS)
    agenda = models.TextField('Agenda', max_length = 1000)      # editable text fields
    workMat = models.TextField('Working Material', max_length = 1000)
    furRead = models.TextField('Further Reading', max_length = 1000)
    
    
