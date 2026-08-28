import logging
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from allauth.account.signals import password_reset
from . models import Profile, PasswordResetLog

# Code generated with AI to listen to Sdjango-allauth and log reset request data.

logger = logging.getLogger('ecommerce.security')

# Automatically create a Profile whenever a new Allauth user registers
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Triggers securely when a user successfully resets their password
@receiver(password_reset)
def log_allauth_password_reset(sender, request, user, **kwargs):
    # Extract client IP securely behind Heroku proxy systems
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_addr = x_forwarded_for.split(',')[0].strip()
    else:
        ip_addr = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    email = user.email if user else "Unknown Email"

    # Log operational status to Heroku stdout console streams
    logger.info(f"Allauth password reset event executed for: {email} from IP: {ip_addr}")

    # Commit audit log securely to database
    PasswordResetLog.objects.create(
        requested_email=email,
        ip_address=ip_addr,
        user_agent=user_agent
    )
# End of AI generated code.