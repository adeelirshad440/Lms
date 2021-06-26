from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Comment, Lesson, Reply


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('lesson_id', 'name', 'position', 'video', 'ppt', 'Notes')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {'body': 'Comments'}

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 70, 'placeholder': 'Enter your comment'})
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body',)

        widgets = {
            'reply_body': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'cols': 10})
        }
