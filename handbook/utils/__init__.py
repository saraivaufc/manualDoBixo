from handbook.models import *
from handbook.forms import *
from handbook.views import *
import base64, os, sys


def getTopicsOrder():
	topics_all = Topic.objects.all()
	if len(topics_all) == 0:
		return []

	topics = []
	positions = sorted(getTopicsPositions())
	for i in positions:
		for k in topics_all:
			if i == k.position:
				topics.append(k)

	for i in topics_all:
		exists = False
		for k in topics:
			if i.id == k.id:
				exists = True
		if exists == False:
			topics.append(i)
	return topics

def getTopicsPositions():
	positions = []
	for i in Topic.objects.all():
		if i.position != None:
			positions.append(i.position)

	return positions

def getItemsNoSets():
		itemsList = []
		for i in Item.objects.all():
			if  len(i.topic.all()) == 0:
				itemsList.append(i)
		return itemsList

def updateVersion():
	try:
		v = Version.objects.get_or_create(name = "handbook")[0]
		number = v.version + 1
		Version.objects.filter(id = v.id).update(version = number)
		return True
	except:
		return False

def imageToJson(url):
	BASE_DIR = os.path.dirname(os.path.dirname(__file__))
	MEDIA_ROOT= os.path.join(BASE_DIR, '..')
	urlImg = MEDIA_ROOT +  url

	with open(urlImg, "rb") as f:
		data = f.read()
		return data.encode("base64")

def topicsToTags(topics):
	tags = ""
	for i in topics:
		tags += (i.title).encode('utf8') + ","
	return tags

#INSERT INTO TOPICO VALUES(NULL, "Infraestrutura do campus");
def topicsAllToSql():
	try:
		topics_model = Topic.objects.all()
		topics_file = open("topics.txt", "w+")
		for i in topics_model:
			topics_file.write(("INSERT INTO TOPICO VALUES(NULL, '%s');\n" % (i.title).encode('utf8')) )
	except:
		return;

#INSERT INTO ITEN VALUES(NULL, "exp_veteranos", "Siglas Malucas", NULL, "sdada");
def itensAllToSql():
	try:
		itens_model = Item.objects.all()
		print len(itens_model)
		itens_file = open("itens.txt", "w+")
		for i in itens_model:
			itens_file.write(("INSERT INTO ITEN VALUES(NULL, '%s', '%s', '%s', '%s');\n" % (i.topic_tag, i.title, i.image_data, i.description )).encode('utf8') )
	except:
		return;