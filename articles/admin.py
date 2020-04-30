from django.contrib import admin
from .models import Article, Section, Member, MemberType, Newsletter, JobPost, NewsletterSubscriber, AwacRegistration

admin.site.register(Article)
admin.site.register(Section)
admin.site.register(Member)
admin.site.register(MemberType)
admin.site.register(Newsletter)
admin.site.register(JobPost)
admin.site.register(NewsletterSubscriber)
admin.site.register(AwacRegistration)
