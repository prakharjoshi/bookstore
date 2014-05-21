from django.contrib import admin
from bookstore.models import book,author,publisher,User


class bookadmin(admin.ModelAdmin):
	list_display = ('name', 'author' , 'publisher','category')
	search_fields = ['name']

class publisheradmin(admin.ModelAdmin):
	list_display = ('name','locality')

"""class signupadmin(admin.ModelAdmin):
	list_display = ('username',)
	search_fields = ['username']

class Useradmin(admin.ModelAdmin):
	list_display = ('username',)"""

"""class MyUserAdmin(UserAdmin):  
    add_form = MyUserCreationForm   

admin.site.register(User,MyUserAdmin)"""


	
admin.site.register(book,bookadmin)
admin.site.register(author)
admin.site.register(publisher,publisheradmin)
#admin.site.register(post)
#admin.site.register(signup,signupadmin)
#admin.site.register(User,Useradmin)

