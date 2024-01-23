from django.contrib import admin
import decimal,csv
from django.http import HttpResponse
#from django.db.models import F

from .models import StudentDetail

# Register your models here.

#@admin.register(CustomerDetail)
class StudentAdmin(admin.ModelAdmin):
	
	list_display=('Name','Email','ContactN','course','place','mode','status','Registeard','Comments')
	#search_fields=CustomerDetail.SearchableFields
	list_filter=["status","course"]
	actions=['export_details']

	def export_details(ModelAdmin,request,queryset):

	
		response=HttpResponse(content_type='text/csv')
		response['Content-Disposition']='attachment; filename=cust_details.csv'
		writer=csv.writer(response)
		writer.writerow(['Name','Email','ContactN','course','place','mode','status','Registeard','Comments'])
		stud_details=queryset.values_list('Name','Email','ContactN','course','place','mode','status','Registeard','Comments')
		for Student in stud_details:
			writer.writerow(Student)
		return response
	export_details.short_description='Download'







  
admin.site.register(StudentDetail,StudentAdmin)