from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render,get_object_or_404,redirect
from . import models,Comm
from .forms import SignUpForm
from .NewItemform import NewItemForm,EditItemForm
from django.db.models import Q
from django.contrib import messages
def index(request):
    items=models.Item.objects.filter(is_sold=False)[0:6]
    categories = models.Category.objects.all()
    return render(request, 'index.html',{
        "categories":categories,
        'items':items
    })
def contact(request):
    return render(request, 'contact.html')
def base(request):
    return render(request,'base.html')
def detail(request, pk):
    item = get_object_or_404(models.Item,pk=pk)

    related_items = models.Item.objects.filter(catagory=item.catagory, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'detail.html',{
        'item':item,
        'related_items':related_items,

        
    })
def signup(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, (" You Were Signuped"))
            return redirect('/login/')
        else:
            return render(request,'signup.html',{
                'form': form
            })
    form=SignUpForm()
    return render(request, 'signup.html',{
        'form': form
    })
@login_required
def new(request):
    if request.method=="POST":
        if request.FILES:
         form=NewItemForm(request.POST,request.FILES)
        else:
            form=NewItemForm(request.POST)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            messages.success(request, ("new item created"))
            return redirect("detail",pk=item.id)
        form.save()
        return render(request, 'form.html',{
        'form': form,
        'title': 'New Item',
    })
    form=NewItemForm()
    return render(request, 'form.html',{
        'form': form,
        'title': 'New Item',
    })
@login_required
def dashboard(request):
    items=models.Item.objects.filter(created_by=request.user)
    return render(request, 'dashboard.html',{
        'items':items
    })
@login_required
def delete(request ,pk):

    itm=get_object_or_404(models.Item,pk=pk, created_by= request.user)
    itm.delete()
    messages.success(request, (" Item was Deleted"))
    return redirect("dashboard")
@login_required
def edit(request,pk):
    itm = get_object_or_404(models.Item, pk=pk, created_by=request.user)
    if request.method=="POST":
        if request.FILES:
         form=EditItemForm(request.POST,request.FILES,instance=itm)
        else:
            form=EditItemForm(request.POST,instance=itm)
        if form.is_valid():
            form.save()
            messages.success(request, ("Edit were done"))
            return redirect("detail",pk=itm.id)
    else:
     form=EditItemForm(instance= itm)
    return render(request, 'form.html',{
        'form': form,
        'title': 'Edit Item',
    })

def item(request):
    query= request.GET.get('query','')
    categories=models.Category.objects.all()
    category_id=request.GET.get('category',0)
    if category_id and query=='':
        items = models.Item.objects.filter(catagory_id=category_id)
    elif category_id and query:
        items = models.Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        items=items.filter(catagory_id=category_id)

    elif query:
         items=models.Item.objects.filter(Q(name__icontains=query)|Q(description__icontains=query))
    else:
     items=models.Item.objects.filter(is_sold=False)

    return render(request,"items.html",{
        'items': items,
        'query': query,
        'categories':categories,
        'category_id':int(category_id),
    })

@login_required
def new_coversation(request,pk):
    item=get_object_or_404(models.Item, pk=pk)
    print("dbfjshbfsf")
    if item.created_by==request.user:
        return redirect('dashboard')
    conversations = models.Conversation.objects.filter(item=item).filter(members__in={request.user.id})
    if conversations:
       return redirect('messages',pk=conversations.first().id)
    if request.method=='POST':
        form=Comm.ConversationMessageForm(request.POST)
        if form.is_valid():
            print("fuck")
            conversation=models.Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            return redirect('detail',pk=pk)
    else:
            form=Comm.ConversationMessageForm()
    return render(request, 'conversation.html',{
            'form':form,
        })

@login_required
def Inbox(request):
    conversations = models.Conversation.objects.filter(members__in=[request.user.id])
    return render(request, 'inbox.html',{
        'conversations':conversations
    })
@login_required
def det(request,pk):
     conversation =models.Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
     if request.method == "POST":
         form=Comm.ConversationMessageForm(request.POST)
         if form.is_valid():
             conversation_message = form.save(commit=False)
             conversation_message.conversation = conversation
             conversation_message.created_by = request.user
             conversation_message.save()
             conversation.save()
             return redirect('messages',pk=pk)
     else:
      form=Comm.ConversationMessageForm()
     return render(request, "message.html",{
         'conversation':conversation,
         'form':form,

     } )
@login_required
def lout(request):
    logout(request)
    messages.success(request," You were loged Out")
    return redirect('index')

