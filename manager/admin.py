
from django.contrib import admin
from .models import StoolCategory, StoolManufacturer, StoolMaterial, Stool, StoolCustomer, StoolOrder, StoolOrderItem, StoolReview

@admin.register(StoolCategory)
class StoolCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(StoolManufacturer)
class StoolManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'website')
    search_fields = ('name', 'country')

@admin.register(StoolMaterial)
class StoolMaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Stool)
class StoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'manufacturer', 'price', 'stock', 'is_available')
    list_filter = ('category', 'manufacturer', 'is_available')
    search_fields = ('name', 'description')

@admin.register(StoolCustomer)
class StoolCustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(StoolOrder)
class StoolOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total_price', 'created_at')
    list_filter = ('status',)
    search_fields = ('customer__first_name', 'customer__last_name')

@admin.register(StoolOrderItem)
class StoolOrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'stool', 'quantity', 'price')
    search_fields = ('stool__name',)

@admin.register(StoolReview)
class StoolReviewAdmin(admin.ModelAdmin):
    list_display = ('stool', 'customer', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('stool__name', 'customer__first_name')