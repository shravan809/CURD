from django.contrib import admin
from .models import Students,issue_book
# Register your models here.
@admin.register(Students)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','roll_number','phone')

@admin.register(issue_book)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'student','book_title','book_author')