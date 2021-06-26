from . import views
from django.urls import path

app_name = 'curriculum'
urlpatterns = [
    path('', views.StandardListView.as_view(), name='standard_list'),
    path('<slug:slug>/', views.SubjectListVIew.as_view(), name='subject_list'),
    path('<str:standard>/<slug:slug>/',
         views.LessonListVIew.as_view(), name='lesson_list'),
    path('<str:standard>/<str:slug>/create/',
         views.LessonCreateListVIew.as_view(), name='lesson_create'),
    path('<str:standard>/<str:subject>/<slug:slug>/',
         views.LessonDetailListVIew.as_view(), name='lesson_detail'),
    path('<str:standard>/<str:subject>/<slug:slug>/update',
         views.LessonUpdateListVIew.as_view(), name='lesson_update'),
    path('<str:standard>/<str:subject>/<slug:slug>/delete',
         views.LessondeleteVIew.as_view(), name='lesson_delete'),

]
