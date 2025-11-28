from django.contrib import admin
from . models import Category, Blog


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
# above two line to generate slug automatically
    list_display = ('title', 'category', 'author', 'is_featured', 'status')
    # above line what items i need to display in the admin dash board
    search_fields = ('id', 'title', 'category__category_name', 'status')
    # what fields i can search the fields - category__ - because it is foreign key
    # cannot put the foreign key fields directly
    list_editable = ('is_featured',)
    # check box functionality in the admin board


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
