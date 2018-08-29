from django.contrib import admin
from . models import Customer,Like,Post,Comments
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
	list_display = ["first_name","last_name","email","mobile","image"]
admin.site.register(Customer,CustomerAdmin)

class PostAdmin(admin.ModelAdmin):
	list_display = ["user","text","image"]
admin.site.register(Post,PostAdmin)

class LikeAdmin(admin.ModelAdmin):
	list_display = ["post","likes","dislikes"]
admin.site.register(Like,LikeAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ["user","post","review","date"]
admin.site.register(Comments,CommentAdmin)