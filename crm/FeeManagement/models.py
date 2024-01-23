from django.db import models
#from django_admin_listfilter_dropdown.filters import DropdownFilter, ChoiceDropdownFilter


# Create your models here.
class MonthlyRegistration(models.Model):
	statusChoices=(
		('Pending','Pending'),
		('Payment completed','Payment completed'),
		
	)
	Paymement_ModeChoices=(
		('CASH','CASH'),
		('UPI','UPI'),
		('NFET','NFET'),
	
	)

	CityChoices=(
		('Bangalore','Bangalore'),
		('Pune','Pune'),
		('Other','Other'),
		
	)

	Batch_DetailChoices=(
		('WEEKDAY ONLINE SESSION','WEEKDAY ONLINE SESSION'),
		('WEEKDAY OFFLINE SESSION','WEEKDAY OFFLINE SESSION'),
		('WEEKEND ONLINE SESSION','WEEKEND ONLINE SESSION'),
		('WEEKEND OFFLINE SESSION','WEEKEND OFFLINE SESSION')

	)

	Invoice1_sendChoices=(
		('Yes','Yes'),
		('No','No'),
		
	)
	Invoice2_sendChoices=(
		('Yes','Yes'),
		('No','No'),
		
	)
	InstallmentsChoices=(
		('First installment','First installment'),
		('Second installment','Second installment'),
		('Third installment','Third installment'),
		

		
	)
	
	
	ID=models.AutoField(primary_key=True,blank=True,unique=True)
	Date=models.DateTimeField(auto_now=False)
	Name=models.CharField(max_length=42)
	PhoneNumber=models.CharField(max_length=42)
	Email=models.EmailField(max_length=70,blank=True,unique=True)
	City=models.CharField(max_length=42,choices=CityChoices)
	course=models.CharField(max_length=42)
	Total_Fee=models.CharField(max_length=42,blank=True)
	Fee_Paid=models.CharField(max_length=42,blank=True)
	Due_Ammount=models.CharField(max_length=42,blank=True)
	Due_Ammount_Date=models.DateTimeField(auto_now=False,blank=True)
	Installments=models.CharField(max_length=42,choices=InstallmentsChoices,blank=True)
	Installments_Date=models.DateTimeField(auto_now=False,blank=True)
	Invoice_send=models.CharField(max_length=42,blank=True,choices=Invoice1_sendChoices)
	Paymement_Mode=models.CharField(max_length=42,blank=True,choices=Paymement_ModeChoices)
	Ammount=models.CharField(max_length=42,blank=True)
	Tax_Ammount=models.CharField(max_length=42,blank=True)	
	Batch_Detail=models.CharField(max_length=42,choices=Batch_DetailChoices)
	status=models.CharField(max_length=42,choices=statusChoices)

	def __str__(self):
		return self.Name


class MonthlyTransaction(models.Model):
	CityChoices=(
		('Bangalore','Bangalore'),
		('Pune','Pune'),
		('Other','Other'),
		
	)
	Payed_to_accountChoices=(
		('Bangalore','Bangalore'),
		('Pune','Pune'),
		('Other','Other'),
		
	)

	Paymement_ModeChoices=(
		('CASH','CASH'),
		('UPI','UPI'),
		('NFET','NFET'),
	
	)

	ID=models.AutoField(primary_key=True,blank=True,unique=True)
	Date=models.DateTimeField(auto_now=False)
	Name=models.CharField(max_length=42)
	PhoneNumber=models.CharField(max_length=42)
	City=models.CharField(max_length=42,choices=CityChoices)
	course=models.CharField(max_length=42)
	Fee_Paid=models.CharField(max_length=42)
	Payed_to_account=models.CharField(max_length=42,choices=Payed_to_accountChoices)	
	PaymentMode=models.CharField(max_length=42,choices=Paymement_ModeChoices)
	Tax=models.CharField(max_length=42,blank=True)
	UPI=models.CharField(max_length=42,blank=True)


	def __str__(self):
		return self.Name









   
   
	