from django.contrib import admin
from bookstore.models import book,author,publisher


class bookadmin(admin.ModelAdmin):
	list_display = ('name', 'author' , 'publisher')
	search_fields = ['name']

class publisheradmin(admin.ModelAdmin):
	list_display = ('name','locality')


admin.site.register(book,bookadmin)
admin.site.register(author)
admin.site.register(publisher,publisheradmin)

