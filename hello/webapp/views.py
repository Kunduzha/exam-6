from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import Commentform
from webapp.models import Comments
# Create your views here.

def main_page(request):
    comment = Comments.objects.all()
    return render(request, "main.html", {'comment': comment})



def add_comment(request):
    if request.method == "GET":
        form = Commentform()
        return render(request, 'add_comment.html', context={'form': form})
    elif request.method == "POST":
        form = Commentform(data=request.POST)
        if form.is_valid():
            comment = Comments.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                comment=form.cleaned_data.get('comment'),
                status=form.cleaned_data.get('status'),

            )
            return redirect('all_page')
        return render(request, 'add_comment.html', context={'form': form})


def dell_comment():
    pass



def update_comment(request, pk):
    comment = get_object_or_404(Good, id=pk)

    if request.method == 'GET':  # если метод запроса GET
        form = Commentform(initial={
            'name': comment.name,
            'email': comment.email,
            'comment': comment.comment,
            'status': comment.status
        })
        return render(request, 'update_comment.html', context={'form': form, 'comment': comment})
    elif request.method == 'POST':
        form = Commentform(data=request.POST)
        if form.is_valid():
            comment.name = form.cleaned_data.get('name')
            comment.email = form.cleaned_data.get('email')
            comment.comment = form.cleaned_data.get('comment')
            comment.status = form.cleaned_data.get('status')

            comment.save()
            return redirect('all_page')
        return render(request, 'update_comment.html', context={'form': form, 'comment': comment})
