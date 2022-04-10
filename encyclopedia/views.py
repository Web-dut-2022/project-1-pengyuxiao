from django.shortcuts import render, redirect
from django import forms
import markdown2
import random

from . import util


class PostForm(forms.Form):
    title = forms.CharField(label='title')
    content = forms.CharField(label='content')


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def detail(request, entry_name):

    content = util.get_entry(entry_name)

    if content is None:
        return render(request, "encyclopedia/error.html", {
            'content': 'Not Found Entry'
        })
    else:
        return render(request, "encyclopedia/detail.html", {
            "entry_name": entry_name,
            "content": markdown2.markdown(content)
        })


def search(request):
    entry_name = request.GET.get('q')
    content = util.get_entry(entry_name)

    if content is None:
        lists = util.list_entries_match(entry_name)
        return render(request, "encyclopedia/index.html", {
            "entries": lists
        })
    else:
        return redirect('/wiki/' + entry_name)


def new_entry(request):
    return render(request, "encyclopedia/create_new.html")


def create_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title) is None:
            util.save_entry(title, content)
            return redirect('/wiki/' + title)
        else:
            return render(request, "encyclopedia/error.html", {
                'content': 'Entry is existed'
            })


def edit(request, entry_name):
    content = util.get_entry(entry_name)
    method = request.method
    if method == 'GET':
        return render(request, "encyclopedia/edit.html", {
            'title': entry_name,
            'content': content,
        })
    elif method == 'POST':
        content = request.POST['content']
        util.save_entry(entry_name, content)
        return redirect('/wiki/' + entry_name)


def random_entry(request):
    lists = util.list_entries()
    entry_num = random.randint(0, len(lists)-1)
    return redirect('/wiki/' + lists[entry_num])

