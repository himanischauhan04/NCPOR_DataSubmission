from django.contrib import admin
from .models import Institute, Project, Expedition, Member, Station

admin.site.register(Institute)
admin.site.register(Project)
admin.site.register(Expedition)
admin.site.register(Member)
admin.site.register(Station)


# Register your models here.
from .models import Metadata

admin.site.register(Metadata)

from .models import Country, State, ScienceCategory, ScienceTopic

admin.site.register(Country)
admin.site.register(State)
admin.site.register(ScienceCategory)
admin.site.register(ScienceTopic)
