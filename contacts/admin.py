from django.contrib import admin
from .models import Person, OrganisationType, Group, Organisation

# admin.site.register(Person)
admin.site.register(OrganisationType)
admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Organisation)



# Register your models here.
