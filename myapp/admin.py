from django.contrib import admin
from myapp.models import *
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(AvailableElection)
admin.site.register(Candidate)
admin.site.register(Vote)
