from django.contrib import admin
from .models import *
# Register your models here.

class LessonAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'course',)

class EnrollmentAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    list_display = ('__str__','user', 'course',)

class CourseAdmin(admin.ModelAdmin):
    search_fields = ('title',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
