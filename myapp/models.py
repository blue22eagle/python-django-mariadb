from django.db import models

# Create your models here.
class myTable(models.Model):
    id= models.IntegerField(primary_key= True)
    FName= models.CharField('First Name', max_length= 50)
    LName= models.CharField('Last Name', max_length= 50)
    BirthDay= models.DateField('Birth Day')
    Age= models.IntegerField('Age')

    class Meta:
        db_table= "myTable"