from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=50,blank=False)  
    ename = models.CharField(max_length=100,blank=False)  
    eemail = models.EmailField(blank=False)  
    econtact = models.CharField(max_length=10,blank=False) 
    def __str__(self):
        return self.ename
 
    class Meta:  
        db_table = "employee"  