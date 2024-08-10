from django.contrib import admin

# Register your models here.
from .models import Listing, LikedListing

class LisitngAdmin(admin.ModelAdmin):
    readonly_fields= ('id', )


class LikedLisitngAdmin(admin.ModelAdmin):
    readonly_fields= ('id', )
    

admin.site.register(Listing, LisitngAdmin)
admin.site.register(LikedListing, LikedLisitngAdmin)
