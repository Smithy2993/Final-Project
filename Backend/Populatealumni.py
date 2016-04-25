import os

def populate():

    add_alumni(first_name = "Bob",last_name = "terrance", course = "Computer Science", faculty = "Faculty of Engineering",sector = "IT",self_employed = "Yes")

def add_alumni(first_name, last_name, course, faculty,sector,self_employed):
    a = alumni.objects.get_or_create(first_name=first_name, last_name=last_name, course=course, faculty=faculty, sector=sector, self_employed=self_employed)[0]
    return a


# Start execution here!
if __name__ == '__main__':
    print ("Starting alumni population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
    from alumni.models import alumni
    populate()
