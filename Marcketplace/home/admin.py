from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category,Item,Conversation,ConversationMessage
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Conversation)
admin.site.register(ConversationMessage)
# Register your models here.
