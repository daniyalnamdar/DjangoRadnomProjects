from django.contrib import admin

# Register your models here.
from .models import *

admin.site.site_header = "Daniyal Admin"
admin.site.site_title = "Ecommerce Daniyal"
admin.site.index_title = "Manage Shopping"



class ProductAdmin(admin.ModelAdmin):

    def changeCategoryToDefault(self,request, queryset):
        queryset.update(category="default")

    changeCategoryToDefault.short_description = 'Default Category'
# in all of them make sure to add comma at the end
    list_display = ('title', 'price', 'discountPrice', 'category', 'description',)
    search_fields = ('title','category',)
    actions = ('changeCategoryToDefault', )
    # which fiels to be shown in detail of admin page
    # fields = ('title',)
    list_editable = ('price',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)