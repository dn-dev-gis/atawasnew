from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Section, Member, MemberType, Newsletter, JobPost, NewsletterSubscriber, AwacRegistration
from .forms import SubscribeForm, AwacRegistrationForm


def home(request):
    home = Article.objects.filter(homepageDisplay=True).order_by('-createDate')[:9]
    blogs = Article.objects.filter(homepageDisplay=True).order_by('-createDate').values_list('pk', flat=True)
    articleCategory = []
    i = 0
    while i < 9:
        a = home[i].category
        articleCategory.insert(i,a)
        i += 1
    articleCategoryTuple = tuple(articleCategory)
    articleCategory0 = articleCategory[0]
    articleCategory1 = articleCategory[1]
    articleCategory2 = articleCategory[2]
    articleCategory3 = articleCategory[3]
    articleCategory4 = articleCategory[4]
    articleCategory5 = articleCategory[5]
    articleCategory6 = articleCategory[6]
    articleCategory7 = articleCategory[7]
    articleCategory8 = articleCategory[8]
    newsletterlatest = Newsletter.objects.order_by('-issue').order_by('-year')[0]
    print(newsletterlatest.issue)
    print(newsletterlatest.year)
    print(newsletterlatest.file)
    return render(request, 'home.html', {'articles':home, 'pk':blogs, 'articleCategory0':articleCategory0, 'articleCategory1':articleCategory1, 'articleCategory2':articleCategory2, 'articleCategory3':articleCategory3, 'articleCategory4':articleCategory4, 'articleCategory5':articleCategory5,'articleCategory6':articleCategory6, 'articleCategory7':articleCategory7, 'articleCategory8':articleCategory8, 'newsletterlatest':newsletterlatest})


def about(request):
    return render(request, 'about.html')


def join(request):
    return render(request, 'join.html')


def members(request):
    members = Member.objects.filter(type__type__contains='Regular').order_by('name')
    amembers = Member.objects.filter(type__type__contains='Affiliate').order_by('name')
    memberscount = Member.objects.filter(type__type__contains='Regular').count()
    amemberscount = Member.objects.filter(type__type__contains='Affiliate').count()
    return render(request, 'members.html', {'members':members, 'amembers':amembers, 'memberscount':memberscount, 'amemberscount':amemberscount,})


def awac(request):
    return render(request, 'awac.html')


def upcomingevents(request):
    upcomingevents = Article.objects.filter(category__category__contains='upcoming events').order_by('-createDate')
    return render(request, 'upcomingevents.html', {'articles':upcomingevents})


def pastevents(request):
    pastevents = Article.objects.filter(category__category__contains='past events').order_by('-createDate')
    return render(request, 'pastevents.html', {'articles':pastevents})


def news(request):
    news = Article.objects.filter(category__category__contains='news').order_by('-createDate')
    return render(request, 'news.html', {'articles':news})


def cdportfolio(request):
    return render(request, 'cdportfolio.html')


def expertgroups(request):
    return render(request, 'expertgroups.html')


def projects(request):
    projects = Article.objects.filter(category__category__contains='projects').order_by('-createDate')
    return render(request, 'projects.html', {'articles':projects})


def newsletter(request):
    newsletters = Newsletter.objects.all().order_by('-year','-issue')
    return render(request, 'newsletter.html', {'newsletters':newsletters})


def publications(request):
    publications = Article.objects.filter(category__category__contains='publications').order_by('-createDate')
    return render(request, 'publications.html', {'articles':publications})


def vacancies(request):
    return render(request, 'vacancies.html')


def jobs(request):
    jobs = JobPost.objects.all().order_by('-postDate')
    return render(request, 'jobs.html', {'jobs':jobs})


def internships(request):
    return render(request, 'internships.html')


def scholarships(request):
    return render(request, 'scholarships.html')


def newslettersubscribe(request):
    if request.method == 'GET':
        return render(request, 'newslettersubscribe.html', {'form':SubscribeForm()})
    else:
        try:
            form = SubscribeForm(request.POST)
            newsubscriber = form.save(commit=False)
            newsubscriber.user = request.user
            newsubscriber.save()
            return redirect('newslettersubscribed')
        except ValueError:
            return render(request, 'newslettersubscribe.html', {'form':SubscribeForm(), 'error':'You already subscribed the ATAWAS Newsletter'})


def newslettersubscribed(request):
    subscriptionemail = NewsletterSubscriber.objects.order_by('-id')[0]
    return render(request, 'newslettersubscribed.html', {'email':subscriptionemail})


def awacregister(request):
    if request.method == 'GET':
        return render(request, 'awacregister.html', {'form':AwacRegistrationForm()})
    else:
        try:
            form = AwacRegistrationForm(request.POST)
            newregistration = form.save(commit=False)
            newregistration.user = request.user
            newregistration.save()
            return redirect('awacregistered')
        except ValueError:
            return render(request, 'awacregister.html', {'form':AwacRegistrationForm(), 'error':'You already registered for AWAC using this email address.'})


def awacregistered(request):
    registrationemail = AwacRegistration.objects.order_by('-id')[0]
    registrationemail2 = registrationemail.email
    return render(request, 'awacregistered.html', {'email':registrationemail2})


def articledetail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles.html', {'article':article})
