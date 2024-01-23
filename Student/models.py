from django.db import models
#from django_admin_listfilter_dropdown.filters import DropdownFilter, ChoiceDropdownFilter


# Create your models here.
class StudentDetail(models.Model):
	statusChoices=(
		('Enquery','Enquery'),
		('Normal_query','Normal_query'),
		('Potential_query','Potential_query'),
		('Cold_query','Cold_query')
	)
	modeChoices=(
         
        ('Offline','Offline'),
        ('Online','Online') 
	)
	RegisteardChoices=(
         
        ('Yes','Yes'),
        ('No','No')
    )


	Name = models.CharField(max_length=42)
	Email = models.EmailField(max_length=70,blank=True,unique=True)
	ContactN = models.IntegerField()
	course=models.CharField(max_length=42)
	place=models.CharField(max_length=42)
	mode=models.CharField(max_length=42,choices=modeChoices)
	status = models.CharField(max_length=42,choices=statusChoices)
	Registeard = models.CharField(max_length=42,choices=RegisteardChoices)
	Comments = models.CharField(max_length=42)
	#export_to_csv =models.BooleanField(default=False)
	DisplayFields=['Name','Email','ContactN','course','place','mode','status','Registeard','Comments']
	SearchableFields=['Name','Email','status']
	FilterFields=['status']



	

	def __str__(self):
		return self.Name
   
   
	