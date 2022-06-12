from django.shortcuts import render,redirect

from .models import Topic,Entry
from .forms import TopicForm,EntryForm
# Create your views here.

def index(request):
    """2班官网的主页"""
    return render(request,'class_2_talker/index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'class_2_talker/topics.html',context)

def topic(request , topic_id):
    #显示单个主题及其所有条目
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request , 'class_2_talker/topic.html',context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据：创建一个新表单
        form = TopicForm()
    else:
        #POST提供的表单无效：对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_2_talker:topics')

    #显示空表单或指出表单无效。
    context = {'form': form}
    return render(request,'class_2_talker/new_topic.html',context)

def new_entry(request, topic_id):
    """在特定主题中增加条目"""
    topic = Topic.objects.get(id=topic_id)


    if request.method !='POST':
        #未提交数据：创建空表单
        form = EntryForm()
    else:
        #POST提交的数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('class_2_talker:topic', topic_id=topic_id)

    #显示空表单或显示空表单无效
    context = {'topic':topic,'form':form}
    return render(request,'class_2_talker/new_entry.html',context)


def edit_entry(request,entry_id):
    """编辑现有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method !='POST':
        #初次请求，使用当前条目表单
        form = EntryForm(instance=entry)
    else:
        #POST提交的数据进行处理
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_2_talker:topic',topic_id=topic.id)

    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'class_2_talker/edit_entry.html',context)
