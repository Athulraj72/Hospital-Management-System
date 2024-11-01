from django.contrib import admin
from .models import categorydb,departmentdb,profiledb,doctordb

admin.site.register(categorydb)
admin.site.register(departmentdb)
admin.site.register(profiledb)
admin.site.register(doctordb)

