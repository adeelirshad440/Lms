from django.http import request
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from .models import Standard, Subject, Lesson
from django.shortcuts import render
from django.views.generic import(
    TemplateView, DetailView, ListView, FormView, CreateView, UpdateView, DeleteView)
from .models import Standard, Subject, Lesson
from .forms import CommentForm, LessonForm, ReplyForm
from django.urls import reverse_lazy

# Create your views here.


class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/standard_list_view.html'


class SubjectListVIew(DetailView):
    # print(Standard.subject)
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/subject_list_view.html'


class LessonListVIew(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'curriculum/lesson_list_view.html'


class LessonDetailListVIew(DetailView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/lesson_detail_view.html'
    second_form_class = ReplyForm
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        return super(LessondeleteVIew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(request=self.request)
        if 'form2' not in context:
            context['form2'] = self.form_class(request=self.request)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)

        if form_name == 'form' and form.is_valid():
            print('Comment is returned')
            return self.form.is_valid(form)
        elif form_name == 'form2' and form.is_valid():
            print('Reply  is returned')
            return self.form2.is_valid(form)

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('curriculum:lesson_list', kwargs={'standard': standard.slug,
                                                              'slug': self.object.slug})

    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.lesson_name = self.object.comments.name
        fm.lesson_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LessonCreateListVIew(CreateView):
    form_class = LessonForm
    context_object_name = 'subject'
    model = Subject
    template_name = 'curriculum/lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('curriculum:lesson_list', kwargs={'standard': standard.slug, 'slug': self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.Subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LessonUpdateListVIew(UpdateView):
    fields = ('name', 'position', 'video', 'ppt', 'Notes')
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/lesson_update.html'


class LessondeleteVIew(DeleteView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/lesson_delete.html'

    def get_success_url(self):
        standard = self.object.Standard
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_list', kwargs={'standard': standard.slug, 'slug': subject.slug})
