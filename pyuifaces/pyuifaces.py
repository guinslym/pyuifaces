import json
import requests
import random

MEN = ["brad_frost", "csswizardry", "guiiipontes", "kurafire", "tomaslau", "cemshid", "dancounsell",
"abecherian", "mlane", "peterme", "suprb", "dingyi", "shalt0ni", "vista", "arminophen",
"kevin_granger", "rssems", "adhamdannaway", "nexy_dre", "teleject", "9lessons", "dakshbhagya",
"_shahedk", "itsjonq", "joshhemsley", "enda", "leemunroe", "vladarbatov", "c_southam", "felipenogs",
"kerem", "ManikRathee", "chadengle", "peterlandt", "jaredfitch", "mattchevy", "soffes", "sindresorhus",
"motherfuton", "mrjohnwalker", "putorti", "teclaro", "andrewaashen", "aaroni", "boheme", "dustinlamont"
]

format_image = {
'bigger' :"https://s3.amazonaws.com/uifaces/faces/twitter/powerpointsuper/73.jpg", 
'normal' :"https://s3.amazonaws.com/uifaces/faces/twitter/powerpointsuper/48.jpg", 
'epic' :"https://s3.amazonaws.com/uifaces/faces/twitter/powerpointsuper/128.jpg", 
'mini' :"https://s3.amazonaws.com/uifaces/faces/twitter/powerpointsuper/24.jpg"
}

size = {'normal': '/48.jpg', 'bigger': '/73.jpg', 'mini': '/24.jpg', 'epic': '/128.jpg'}

class PyUIFaces(object):

		def __init__(self, network=False, username='random', image_size="epic", link=""):
				self._network = network
				self._username = username
				self._image_size   = size[image_size]
				self._link = "http://uifaces.com/api/v1/user/"

		def face(self):
				if self._network == False and self._username == 'random': #return random.choice(MEN)
						#select a user from USERNAME[] and make up a link
						return self._link + random.choice(MEN) + self._image_size#local_random(image_size)
				#retrieve a specific link
				else:
						try:
								resp = requests.get(url="http://uifaces.com/api/v1/random")
						except requests.exceptions.ConnectionError, e:
								return self._link + random.choice(MEN) + self._image_size

						if resp.ok:
								data = json.loads(resp.text)
								return self._link  + data['username'] + self._image_size
						else:
								return self._link + random.choice(MEN) + self._image_size

		def man(self):
				return self._link + random.choice(MEN) + self._image_size

		def woman(self):
				return self._link + random.choice(MEN) + self._image_size

foo = PyUIFaces(True, 'random', 'normal')
print(foo.face())

