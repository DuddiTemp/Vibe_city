from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    discord_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    discord_username = models.CharField(max_length=100, null=True, blank=True)
    discord_discriminator = models.CharField(max_length=10, null=True, blank=True)
    discord_avatar = models.CharField(max_length=255, null=True, blank=True)
    is_whitelisted = models.BooleanField(default=False)
    is_staff_member = models.BooleanField(default=False)
    
    # --- Job Review Permissions --- #
    can_review_sasp = models.BooleanField(_("Can Review SASP Apps"), default=False)
    can_review_ems = models.BooleanField(_("Can Review EMS Apps"), default=False)
    can_review_mechanic = models.BooleanField(_("Can Review Mechanic Apps"), default=False)

    # --- Employment Status --- #
    is_sasp_employee = models.BooleanField(_("Is SASP Employee"), default=False)
    is_ems_employee = models.BooleanField(_("Is EMS Employee"), default=False)
    is_mechanic_employee = models.BooleanField(_("Is Mechanic Employee"), default=False)
    
    def __str__(self):
        if self.discord_username:
            return f"{self.discord_username}#{self.discord_discriminator}"
        return self.username
    
    @property
    def discord_tag(self):
        if self.discord_username and self.discord_discriminator:
            return f"{self.discord_username}#{self.discord_discriminator}"
        return None
    
    @property
    def avatar_url(self):
        print(f"DEBUG: ID={self.discord_id}, Avatar={self.discord_avatar}")  # Debugging
        
        if self.discord_avatar:
            file_format = "gif" if self.discord_avatar.startswith("a_") else "png"
            return f"https://cdn.discordapp.com/avatars/{self.discord_id}/{self.discord_avatar}.{file_format}"
        
        fallback_index = int(self.discord_discriminator) % 5 if self.discord_discriminator else 0
        return f"https://cdn.discordapp.com/embed/avatars/{fallback_index}.png"

