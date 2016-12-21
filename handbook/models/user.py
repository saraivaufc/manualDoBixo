from django.db import models
from django.conf import settings

# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.models import Group, Permission

try:
    from hashlib import md5
except:
    from md5 import new as md5

class PersonManager(UserManager):
    def create_user(self, email, password=None, group='general', **extra_fields):
        print 'create_user'
        email = email
        user = self.model(
            email = email,
        )
        user.set_password(password)
        user.save(group= group)
        return user

    def create_superuser(self, email, password , **extra_fields):
        print 'create_superuser'
        user = self.create_user(email, password, 'organizer')
        user.is_superuser = True
        user.is_moderator = True
        user.is_staff = True
        user.save()
        return user

class AbstractSystemPerson(models.Model):
    location = models.CharField(_(u"location"), max_length=75, blank=True, null=True)
    last_seen = models.DateTimeField(_(u"last seen"), auto_now=True)
    last_ip = models.GenericIPAddressField(_(u"last ip"), blank=True, null=True)
    #is_superuser = models.BooleanField(_('administrator status'), default=False,blank=True )
    is_moderator = models.BooleanField(_('moderator status'), default=False, blank=True)
    is_staff = models.BooleanField(_(u'staff status'), default=False,
                                   help_text=_(u'Designates whether the user can log into this admin site.'))
    

    def get_location(self):
        return self.location
    
    def get_last_seen(self):
        return self.last_seen
    
    def get_last_ip(self):
        return self.last_ip
    
    def save(self, *args, **kwargs):
        super(AbstractSystemPerson, self).save(*args, **kwargs)
        
    
    class Meta:
        abstract = True

class AbstractPerson(AbstractBaseUser, PermissionsMixin, AbstractSystemPerson):
    first_name = models.CharField(_(u"First Name "), max_length=100, blank=False,null=True,help_text=_(u'Please enter you first name.'),)
    last_name = models.CharField(_(u"Last Name "), max_length=100, blank=False,null=True,help_text=_(u'Please enter you last name.'),)
    email = models.EmailField(_(u"Email"), max_length=254, unique=True, blank=False, help_text=_(u'Please enter you email.'),)
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_(u'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_(u'date joined'), default=timezone.now)
    objects = PersonManager()

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        if self.get_first_name():
            if self.get_last_name():
                return self.get_first_name() + " " + self.get_last_name()
            else:
                return self.get_first_name()
        else: 
           return self.get_email()
    def get_short_name(self):
        if self.get_first_name():
            return self.get_first_name()
        else:
            return self.get_email()


    def get_email(self):
        return self.email
    
    def get_date_joined(self):
        return self.date_joined

    def delete(self):
        self.is_active = False
        self.save()
        
    def restore(self):
        self.is_active = True
        self.save()

    USERNAME_FIELD = 'email'
    
    def __unicode__(self):
        return self.get_full_name()

    class Meta:
        abstract = True            
        
    def change_password(self, new_password):
        new_password_hash = md5(new_password).hexdigest()
        self.password = new_password_hash
        self.save()  
        


class Person(AbstractPerson):
    profile_image = models.ImageField(verbose_name=_(u"Profile Image"),help_text=_(u"Please enter you profile image."),upload_to = 'documents/image/profile_image/%Y/%m/%d', null=True, blank=True, default=None)

    def save(self,group=None, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        if not group and not self.groups.all():
            group = 'general'
        if group and not self.groups.all():
            print 'Create user with group=', group
            group = Group.objects.get(name=group)
            self.groups.add(group)

    
    def get_groups(self):
        return self.groups.all()
    

    def get_profile_image(self):
        return self.profile_image
    
    def __unicode__(self):
        return self.get_full_name()

    
    class Meta(AbstractPerson.Meta):
        abstract = False
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'
        app_label = 'handbook'
        ordering = ['-date_joined', ]
        verbose_name = _(u'Person')
        verbose_name_plural = _(u'Persons')
   
class General(Person):

    def __unicode__(self):
        return self.get_email()

    class Meta(Person.Meta):
        verbose_name = _('General User')
        verbose_name_plural = _('General Users')

class Organizer(Person):

    def __unicode__(self):
        return self.get_email()

    class Meta(Person.Meta):
        verbose_name = _('Organizer')
        verbose_name_plural = _('Organizes')
        