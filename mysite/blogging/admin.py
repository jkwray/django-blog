from django.contrib import admin
from blogging.models import Post, Category

# class CategoryInline(admin.TabularInline):
#     # model = Category
#     pass

# class PostAdmin(admin.ModelAdmin):
#     inlines = [CategoryInline, ]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
