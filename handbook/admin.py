from django.contrib import admin
from handbook.models.access import OrganizerKey
from handbook.models.contact import Contact
from handbook.models.item import Item
from handbook.models.topic import Topic
from handbook.models.user import Person, General, Organizer
from handbook.models.version import Version

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	pass
@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
	pass
@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
	pass
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
	pass
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	pass
@admin.register(OrganizerKey)
class OrganizerKeyAdmin(admin.ModelAdmin):
	pass
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	pass
@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
	pass