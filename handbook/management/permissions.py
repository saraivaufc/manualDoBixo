from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

from django.db.models import signals
from handbook.models import Person, General, Organizer 


from handbook import models

permissions = {}

group_permissions = {
	"organizer": [],
	"general": [],
}



def create_user_groups(app, created_models, verhandbooksity=1, **kwargs):
	if verhandbooksity > 0:
		print "Initialising data post_syncdb"
	
	for group in group_permissions:
		if group == 'organizer':
			model = Organizer
		elif group == 'general':
			model = General
		else:
			model = General
		content_type = ContentType.objects.get_for_model(model)

		role, created = Group.objects.get_or_create(name=group)
		if verhandbooksity > 1 and created:
			print 'Creating group', group
		for perm in group_permissions[group]:
			perm, created = Permission.objects.get_or_create(codename=perm, name=permissions[perm], content_type=content_type)
			role.permissions.add(perm)
			if verhandbooksity > 1:
				print 'Permitting', group, 'to', perm
		role.save()



signals.post_syncdb.connect(
    create_user_groups, 
    sender=models,
    dispatch_uid='handbook.models.create_user_groups'
)