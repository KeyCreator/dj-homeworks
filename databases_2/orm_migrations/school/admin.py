from django.contrib import admin

from .models import Student, Teacher

class TeacherInline(admin.TabularInline):
    model = Student.teacher.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [TeacherInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [TeacherInline]


# admin.site.register(Student, StudentAdmin)
# admin.site.register(Teacher, TeacherAdmin)


