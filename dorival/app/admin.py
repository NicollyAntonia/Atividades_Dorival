from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAbs
# Register your models here.

class UserAbsAdmin(UserAdmin):
    list_display = ('username','email', 'biografia','idade', 'telefone','endereco','escolaridade','quantidade_animals'  'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('biografia','idade', 'telefone','endereco','escolaridade','quantidade_animals' )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('email')}),
    )

admin.site.register(UserAbs, UserAbsAdmin)
