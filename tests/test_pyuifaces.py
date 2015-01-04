#!/usr/bin/env python

import json
import requests
import random
import unittest
from unittest import TestCase



class TestGetaLink(TestCase):
    def test_is_link_is_a_string(self):
        foo = PyUIFaces(False, 'random', 'mini')
        foo = foo.face()
        self.assertTrue(isinstance(foo, str))
    def test_is_image_format_is_24_jpg(self):
        foo = PyUIFaces(False, 'random', 'mini')
        foo = foo.face().split("/")[-1]
        self.assertTrue(foo, '24.jpg')
    def test_is_default_image_format_is_128_jpg(self):
        foo = PyUIFaces(False, 'random', 'wrong_image_input')
        foo = foo.face().split("/")[-1]
        self.assertTrue(foo, '128.jpg')
    def test_is_man_image_is_in_MEN_array(self):
        foo = PyUIFaces(False, 'random')
        man = foo.man().split("/")[-2]
        self.assertTrue(man in foo.MEN)
    def test_is_woman_image_is_in_WOMEN_array(self):
        foo = PyUIFaces(False, 'random')
        woman = foo.woman().split("/")[-2]
        self.assertTrue(woman in foo.WOMEN)
    def test_if_Network_is_down_username_is_in_USERNAME(self):
    		foo = PyUIFaces(True, 'guinslym')
    		#locally I turn off my network to verify this
    		username = foo.face().split("/")[-2]
    		self.assertTrue(username in foo.USERNAME)



class PyUIFaces(object):

		USERNAME= ['brad_frost', 'iflendra', 'kastov_yury', 'vladabazhan', 'csswizardry', 'eduardo_olv', 
		'vladarbatov', 'mizko', 'kurafire', 'shalt0ni', 'sachagreif', 'dancounsell', 
		'adhamdannaway', 'peterlandt', 'chadengle', 'pixeliris', 'whale', 'kerem', 'ateneupopular', 
		'boheme', 'cemshid', 'thrivesolo', 'enda', 'jollynutlet', 'adellecharles', 'peterme', 'mghoz', 
		'flamekaizar', 'jina', 'dustinlamont', 'idiot', 'joshhemsley', 'mlane', 'nexy_dre', 'sindresorhus', 
		'sillyleo', 'motherfuton', 'tomaslau', 'arminophen', 'guiiipontes', 'c_southam', 
		'mrjohnwalker', 'iconfinder', 'glif', '_hartjeg', 'soffes', 'teleject', 'brynn', 
		'rssems', 'felipenogs', 'gt', 'mattchevy', 'jaredfitch', 'andrewaashen', 'ladylexy', 
		'brandclay', 'abecherian', 'ManikRathee', 'vista', 'leemunroe', 'dingyi', 'putorti', 
		'dakshbhagya', 'dannpetty', 'teclaro', '_shahedk', 'kfriedson', 'kevin_granger', 'fffabs', 
		'pinceladasdaweb', 'suprb', '9lessons', 'itsjonq', 'aaroni', '_everaldo',"canrec", "carloscrvntsg",
		"reetajayendra", "pbaranco", "likewings", "delanicete", "joshkennedy", "xadusx", "nadezdaneverova",
		"i_ganin", "derekcramer", "raphaelnikson", "zombieoummy", "shiienurm", "sunnsit", "jonathanchrisp",
		"joelcannon", "bangherisetiawn", "pburjanec", "hilanimal", "massfocus", "c_southam", 
		"noammorrissey", "davidsasda", "_eyev_", "j04ntoh", "vm_f", "shaan360", "gmourier", 
		"rikitanone", "akmur", "moaazsidat", "bernieaho", "grysnsmth", "timoliverau", "rowancavanagh",
		"damirdurmo", "meecasso", "hathawaystephen", "craftbynick", "dland", "pjnes", "balintorosz",
		"903886562", "roskin_m", "trucy", "albertaugustin", "yalozhkin", "codysanfilippo", "dutchnadia",
		"kilperic", "pequelord", "hoangloi", "islamgaraev_tim", "superoutman", "shiienurm", "josue", 
		"joelcannon", "glauberamos", "jayvisavadia", "karalek", "embrcecreations", "amoslanka", 
		"damirdurmo", "alemasferrer", "willrax", "jehnglynn", "masterhopia316", "glauberamos", 
		"rasagy", "fireupman", "ravikumar8", "kimberlygs_", "lososina", "n2kza", "bagawarman", 
		"andyfang98", "viktor_dotsenko", "irfansami2", "timbalabuch", "monicaczarny", "moae84", 
		"autobanshaq", "marissamcpeak", "carlosblanco_eu", "ddddrew", "htmlstream", "tofslie", 
		"amlinarev", "saarabpreet", "svenphan", "scottfister", "funwatercat", "ya_zl01", 
		"pauljakobwhite", "areus", "cookingeasycom", "kirangopal", "grantharr_s", "rpatey",
		"aaronstump", "dfhdesign", "hejallan", "pf_creative", "rikas", "spacewood_", "sava2500", "sebygarilli", 
		"dustintheweb", "colynb", "linkinf88k", "wilsonnma", "lettershoppe", "vipinsanker", "spencerortega", 
		"soh3il", "he_jinsheng", "tomgreever", "meisso_jarno", "lukaszklis", "robturlinckx", "looneydoodle", 
		"alxleroydeval", "mizhgan", "kimberlygs_", "vista", "raresloth", "ntfblog", "j1tang", "jefffis", "jehnglynn", 
		"tgormtx", "dan_malarkey", "amoslanka", "mrmartineau", "kaibrach", "skylark64", "antjanus", "kirillgreen", 
		"brenton_clarke", "matejlatin", "froidz", "nickyzoid", "dreierdominic", "skogberg", "joelcipriano", 
		"inspiringbg", "donschnelly", "thimo_cz", "russell_baylis", "mashaaaaal", "areskub", "csteib", "petebernardo", 
		"ilya101010", "jckieangel", "jjsiii", "onkaar", "jbcordina", "lalalaura922", "heyllowlab", "nadya_lex", "suprb", 
		"pinceladasdaweb", "edwin_de_jongh", "francortz", "indigo90", "vishal19801", "jozh123", "anton0kurilov", 
		"originalgoatee", "chendahang", "alestart", "jningtho", "antongenkin", "turkutuuli", "razlagutt", "nepdud", 
		"snowshade", "nate_designer", "peachananr", "shuangshuangli", "quisif", "mrgnw", "devineninaresh", 
		"nathansimpsongd", "bruno1fernando", "mrxloka", "arpad05", "gunjanraik", "mangosango", "adellecharles", 
		"rikyushinichi", "ramdreamers", "victinx", "lingeswaran", "codydmd", "chexee", "sorenschroder", "zeppeppers", 
		"cotegrunenwald", "leelkennedy", "abujahed19", "dahparra", "borryshasian", "leogono", "ianlopshire", 
		"marciotoledo", "didpopcom", "fidelthomet", "ahmedelgabri", "andrewofficer", "ceekaytweet", "shanya_o", 
		"aarondgilmore", "herrhaase", "sikeane", "creativebrainbe", "jrxmember", "limpa123", "rbaassi", "haydn_woods", 
		"puzik", "i_makethings", "olgary", "arminophen", "and_zmei", "mkosterich", "suggeelson", "ektadary", 
		"nansysweet2", "tristandenyer", "aluisio_azevedo", "areandacom", "allenjordan", "hichamazhairi", "sachingawas", 
		"thekennythegame", "vashokk", "cattsmall", "elliotnolten", "tyagoneres", "mikewilliam1982", "n_tassone", 
		"rok_samsa", "eitarafa", "lucassimons1987", "maks_akmal", "007aasim", "phaistonian", "georgedyjr", 
		"gcmorley", "azizarsl", "flobota", "adamkirkwood", "creative_px", "sannigraphics", "kurtinc", "superhankai", 
		"strelov_d", "paladinstudio", "richwild", "rv_atom", "vlysergin", "mostafahawary", "gavr1l0", "umairulhaque", 
		"typografil", "spacekid", "seomarlboro", "chinagrimace", "deedubs", "marcosnwp", "hollymdewolf", "boundbystars", 
		"mrjohnwalker", "seantremaine", "jghyllebert", "the_frug", "solid_color", "pampersdry", "elcardoson", 
		"lisakey1986", "michaelcomiskey", "gordo", "olivermonschau", "davidmerrique", "plbabin", "mattdetails", 
		"michaelbrooksjr", "ariona_rian", "davidvb", "gokhunguneyhan", "brad_frost", "islamgaraev_tim", "kennyadr", 
		"ahmed_sa3ied", "simply_simpy", "bwagert", "gearoidorourke", "evgeny_ryabcev", "zackeeler", "ooomz", 
		"richcsmith", "raydeguzmanto", "jemmoudimed", "asna_farid", "davidhemphill", "joshuarule", "dreizle", "dannegm", 
		"majksner", "fgin69", "_zm", "motionthinks", "ShaneHelm", "bgiardelli", "ntnth", "avnagaraj", "stephenmdixon", 
		"jolliver", "osmond", "matthewkay_", "powerpointsuper", "itsselvam", "alexanderkirov", "brandon_arnold", 
		"julesholleboom", "laksgandikota", "kristoffintosh", "prheemo", "sconzen", "tazmattar", "mobfrank", 
		"alek_djuric", "normanbox", "konvictedofsin", "boheme", "aeon56", "gofrasdesign", "andresenfredrik", "upslon", 
		"jonpyefinch", "itsjaymem", "vamseekrishnain", "dsaltaren", "bbergher", "jackiesaik", "cheezonbread", 
		"onlymagugz", "kokikillara", "pavelbuben", "babojan", "thaoalpha1501", "lososina", "michaelcecetka", 
		"zensenmobile", "thramp", "Chakintosh", "jiceb", "aviddayentonbay", "depaulawagner", "sweetdelisa", 
		"kadri1914", "tomreinhoudt", "fionaosaurusrex", "robergd", "bbuecherl", "nicoleglynn", "hellofeverrrr", 
		"jasonkempers", "sterlingrules", "anysmechkar", "loresrockstar", "victorabrantes", "ilucasramos", "bartjo", 
		"motamarad", "deluzino", "jay_wilburn", "lpzilva", "migl40d", "_iamnyasha", "vitorleal", "edhenderson", 
		"akmalfikri", 'guinslym']

		MEN = ["brad_frost", "csswizardry", "guiiipontes", "kurafire", "tomaslau", "cemshid", "dancounsell",
		"abecherian", "mlane", "peterme", "suprb", "dingyi", "shalt0ni", "vista", "arminophen",
		"kevin_granger", "rssems", "adhamdannaway", "nexy_dre", "teleject", "9lessons", "dakshbhagya",
		"_shahedk", "itsjonq", "joshhemsley", "enda", "leemunroe", "vladarbatov", "c_southam", "felipenogs",
		"kerem", "ManikRathee", "chadengle", "peterlandt", "jaredfitch", "mattchevy", "soffes", "sindresorhus",
		"motherfuton", "mrjohnwalker", "putorti", "teclaro", "andrewaashen", "aaroni", "boheme", "dustinlamont"
		]

		WOMEN = ["jina", "ladylexy", "adellecharles", "kfriedson", "brynn", "pixeliris", "nisaanjani"]


		def __init__(self, network=False, username='random', image_size="epic"):
				self._network = network
				self._username = username
				self._image_size   = {'normal': '/48.jpg', 
														'bigger': '/73.jpg', 
														'mini': '/24.jpg', 
														'epic': '/128.jpg'}.get(image_size, '/128.jpg')
				self._link = "http://uifaces.com/api/v1/user/"

		def face(self):
				if self._network == False and self._username == 'random': #return random.choice(MEN)
						#select a user from USERNAME[] and make up a link
						return self._link + random.choice(self.USERNAME) + self._image_size#local_random(image_size)
				#retrieve a specific link
				else:
						try:
								resp = requests.get(url="http://uifaces.com/api/v1/random")
						except requests.exceptions.ConnectionError as e:
								return self._link + random.choice(self.USERNAME) + self._image_size

						if resp.ok:
								data = json.loads(resp.text)
								return self._link  + data['username'] + self._image_size
						else:
								return self._link + random.choice(self.USERNAME) + self._image_size

		def man(self):
				return self._link + random.choice(self.MEN) + self._image_size

		def woman(self):
				return self._link + random.choice(self.WOMEN) + self._image_size











############################################################



if __name__ == '__main__':
		unittest.main()
