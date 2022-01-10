from django.db import models
class Studentinfo(models.Model):
    roll_no = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=50,verbose_name='Student Name')
    clas    = models.IntegerField(verbose_name="Class")
    school  = models.CharField(max_length=200,verbose_name="School Name")
    mobile  = models.PositiveIntegerField(verbose_name="Student Mobile Number")
    address = models.TextField(verbose_name="Address")

    def __str__(self):
        return self.name

class StudentAcademics(models.Model):
    stu_acad_id = models.AutoField(primary_key=True)
    roll_no_id  = models.ForeignKey(Studentinfo,on_delete=models.CASCADE)
    math        = models.IntegerField(verbose_name="Maths Marks")
    physics     = models.IntegerField(verbose_name="Physics Marks")
    chemistry   = models.IntegerField(verbose_name="Chemistry Marks")
    biology     = models.IntegerField(verbose_name="Biology Marks")
    english     = models.IntegerField(verbose_name="English Marks")

