from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project
from .forms import ProjectForm, RaiseAmountForm


def projects_list(request):
    project_list = Project.objects.all()
    paginator = Paginator(project_list, 5)
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    context = {
        'projects': projects,
    }
    return render(request, 'projects/list.html', context)



def single_project(request, slug=None):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        form = RaiseAmountForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            project.amountRaised += amount
            project.save()
            return redirect('projects_list')
    else:
        form = RaiseAmountForm()
    context = {
        'project': project,
        'form': form,
    }
    return render(request, 'projects/single.html', context)


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.creator = request.user
            project.save()
            return redirect('projects_list')
    else:
        form = ProjectForm()
    context = {
        'form': form,
    }
    return render(request, 'projects/project_form.html', context)


@login_required
def edit_project(request, slug=None):
    project = get_object_or_404(Project, slug=slug)
    if request.user != project.creator:
        raise PermissionDenied
    form = ProjectForm(request.POST or None, request.FILES or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('projects_list')
    context = {
        'form': form,
    }
    return render(request, 'projects/project_edit_form.html', context)


@login_required
def delete_project(request, slug=None):
    project = get_object_or_404(Project, slug=slug)
    if request.user != project.creator:
        raise PermissionDenied
    project.delete()
    return redirect('projects_list')

from datetime import datetime

@login_required
def my_projects(request):
    inactive_projects = Project.objects.filter(creator=request.user).filter(finish__lt=datetime.now())
    active_projects = Project.objects.filter(creator=request.user).filter(finish__gte=datetime.now())
    context = {
        'active_projects': active_projects,
        'inactive_projects': inactive_projects,
    }
    return render(request, 'projects/my_list.html', context)
