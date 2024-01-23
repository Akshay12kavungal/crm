
from django.contrib import admin
import decimal,csv
from django.http import HttpResponse
#from django.db.models import F

from .models import MonthlyRegistration,MonthlyTransaction


# Register your models here.

#@admin.register(MonthlyRegistration)
class StudentAdmin(admin.ModelAdmin):
	
	list_display=('ID','Date','Name','PhoneNumber','Email','City','course','Total_Fee','Fee_Paid','Due_Ammount','Due_Ammount_Date','Installments','Installments_Date','Invoice_send','Paymement_Mode','Ammount','Tax_Ammount','Batch_Detail','status')
	#search_fields=CustomerDetail.SearchableFields
	list_filter=["City","Date","status"]
	actions=['export_details']

	def export_details(ModelAdmin,request,queryset):

	
		response=HttpResponse(content_type='text/csv')
		response['Content-Disposition']='attachment; filename=Monthly Registration.csv'
		writer=csv.writer(response)
		writer.writerow(['ID','Date','Name','PhoneNumber','Email','City','course','Total_Fee','Fee_Paid','Due_Ammount','Due_Ammount_Date','Installments','Installments_Date','Invoice_send','Paymement_Mode','Ammount','Tax_Ammount','Batch_Detail','status'])
		stud_details=queryset.values_list('ID','Date','Name','PhoneNumber','Email','City','course','Total_Fee','Fee_Paid','Due_Ammount','Due_Ammount_Date','Installments','Installments_Date','Invoice_send','Paymement_Mode','Ammount','Tax_Ammount','Batch_Detail','status')
		for Student in stud_details:
			writer.writerow(Student)
		return response
	export_details.short_description='Download'
class MonthlyTransactionAdmin(admin.ModelAdmin):
	
	list_display=('ID','Date','Name','PhoneNumber','City','course','Fee_Paid','Payed_to_account','PaymentMode','Tax','UPI')
	#search_fields=CustomerDetail.SearchableFields
	list_filter=["Date","City"]

	actions=['export_details']

	def export_details(ModelAdmin,request,queryset):

		
		response=HttpResponse(content_type='text/csv')
		response['Content-Disposition']='attachment; filename=Monthly Transaction.csv'
		writer=csv.writer(response)
		writer.writerow(['ID','Date','Name','PhoneNumber','City','course','Fee_Paid','Payed_to_account','PaymentMode','Tax','UPI'])
		trans_details=queryset.values_list('ID','Date','Name','PhoneNumber','City','course','Fee_Paid','Payed_to_account','PaymentMode','Tax','UPI')
		for FeeManagement in trans_details:
			writer.writerow(FeeManagement)
		return response
	export_details.short_description='Download'


admin.site.register(MonthlyRegistration,StudentAdmin)
admin.site.register(MonthlyTransaction,MonthlyTransactionAdmin)