from helloworld.models import Person  


for i in range(100):
    eu = Person(name=('Robert' + str(i+1)), varsta=i+1)
    eu.save()

Person.objects.values()