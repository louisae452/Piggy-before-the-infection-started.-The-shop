from django.contrib import admin
from .models import PasswordResetLog, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country')
    search_fields = ('user__username', 'user__email')


# Code generated with AI to record password reset requests.
@admin.register(PasswordResetLog)
class PasswordResetLogAdmin(admin.ModelAdmin):
    list_display = ('requested_email', 'ip_address', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('requested_email', 'ip_address')
    # Make logs read-only in admin so they can't be tampered with
    readonly_fields = ('requested_email', 'ip_address',
                       'user_agent', 'timestamp')
# End of AI generated code.
