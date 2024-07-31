from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Category(models.Model):
 name=models.CharField(max_length=255)
 class Meta:
   ordering=("name",)
   verbose_name_plural="categories"
 def __str__(self):
  return self.name
class Item(models.Model):
 catagory=models.ForeignKey(Category,related_name="item",on_delete=models.CASCADE)
 name=models.CharField(max_length=255)
 description=models.TextField(blank=True,null=True)
 price=models.FloatField()
 image=models.ImageField(blank=True,null=True)
 is_sold=models.BooleanField(default=False)
 created_by=models.ForeignKey(User,related_name="item",on_delete=models.CASCADE)
 created_at=models.DateTimeField( auto_now_add=True)
 def __str__(self):
  return self.name
class Conversation(models.Model):
 item=models.ForeignKey(Item, related_name='conversation',on_delete=models.CASCADE)
 members=models.ManyToManyField(User,related_name='conversation')
 created_at=models.DateTimeField(auto_now_add=True)
 modified_at=models.DateTimeField(auto_now=True)
 class Meta:
   ordering=("-modified_at",)

class ConversationMessage(models.Model):
 conversation=models.ForeignKey(Conversation, related_name='messages',on_delete=models.CASCADE)
 content=models.TextField()
 created_at = models.DateTimeField(auto_now_add=True)
 created_by=models.ForeignKey(User,related_name="created_messages",on_delete=models.CASCADE)


