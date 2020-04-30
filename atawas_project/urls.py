from django.contrib import admin
from django.urls import path, include
from articles import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # admin
    path('admin/', admin.site.urls),

    # home
    path('', views.home, name='home'),

    # static pages main menu
    path('about/', views.about, name='about'),
    path('join/', views.join, name='join'),
    path('awac/', views.awac, name='awac'),
    path('members/', views.members, name='members'),
    path('cdportfolio/', views.cdportfolio, name='cdportfolio'),
    path('expertgroups/', views.expertgroups, name='expertgroups'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('jobs/', views.jobs, name='jobs'),
    path('internships/', views.internships, name='internships'),
    path('scholarships/', views.scholarships, name='scholarships'),

    # static pages other
    path('awacregister/', views.awacregister, name='awacregister'),
    path('awacregistered/', views.awacregistered, name='awacregistered'),
    path('newslettersubscribe/', views.newslettersubscribe, name='newslettersubscribe'),
    path('newslettersubscribed/', views.newslettersubscribed, name='newslettersubscribed'),


    # dynamic pages (articles)
    path('upcoming/', views.upcomingevents, name='upcomingevents'),
    path('past/', views.pastevents, name='pastevents'),
    path('projects/', views.projects, name='projects'),
    path('publications/', views.publications, name='publications'),
    path('news/', views.news, name = 'news'),
    path('articles/<int:article_id>/', views.articledetail, name='articledetail'),


    # contact database
    path('contactdb/', include('contacts.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
