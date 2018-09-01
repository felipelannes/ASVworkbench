from django.contrib import admin
from .models import VESSEL, PART

# Register your models here.

@admin.register(VESSEL)
class VESSEL_ADMIN(admin.ModelAdmin):

	list_display = ['name', 'project_number', 'created_at']
	prepopulated_fields = {'slug':('name',)}


@admin.register(PART)
class PART_ADMIN(admin.ModelAdmin):
	list_display = ['vessel_id','group_system', 'part_name', 'description']

