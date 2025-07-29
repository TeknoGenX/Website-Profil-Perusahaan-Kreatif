from django.contrib import admin
from .models import Service, Portfolio, TeamMember, Testimonial, CompanyInfo

admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(TeamMember)
admin.site.register(Testimonial)
admin.site.register(CompanyInfo)
