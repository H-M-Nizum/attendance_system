from django.contrib import admin
from .models import StudentModel, classModel
# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name', 'slug']
    
    
admin.site.register(classModel, ClassAdmin)
admin.site.register(StudentModel)