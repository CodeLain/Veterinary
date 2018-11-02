from django.contrib import admin
from storeCore.models import AnimalType, AnimalBrand, Pet, Owner, Veterinary
from django.contrib.auth.admin import UserAdmin
from .forms import OwnerChangeForm, OwnerCreationForm, VeterinaryCreationForm, VeterinaryChangeForm


class OwnerAdmin(UserAdmin):
    # The forms to add and change user instances
    form = OwnerChangeForm
    add_form = OwnerCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'username', 'email',)
    # readonly_fields = ('activation_token',)
    # list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Account Info', {'fields': ('avatar', 'username', 'is_active')}),
        # ('tokens', {'fields': ('token',)}),
        # ('Permissions', {'fields': ('',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Account Info', {'fields': ('avatar', 'username', 'is_active')}),
        # ('Tokens', {'fields': ('token',)}),
        # ('Permissions', {'fields': ('',)}),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()


class VeterinaryAdmin(OwnerAdmin):
    form = VeterinaryChangeForm
    add_form = VeterinaryCreationForm


admin.site.register(Owner, OwnerAdmin)
admin.site.register(AnimalType)
admin.site.register(AnimalBrand)
admin.site.register(Pet)
admin.site.register(Veterinary, VeterinaryAdmin)


