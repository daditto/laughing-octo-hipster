
# if UnicodeEncodeError happens
# use this in the console: chcp 65001

import urllib.request
from bs4 import BeautifulSoup

urls = [
	'http://hackuci.challengepost.com/submissions/23944-snap-map',
	'http://hackuci.challengepost.com/submissions/23945-hiddenlist',
	'http://hackuci.challengepost.com/submissions/23946-shockerstalker',
	'http://hackuci.challengepost.com/submissions/23948-ben-d3r',
	'http://hackuci.challengepost.com/submissions/23954-virtual-classroom',
	'http://hackuci.challengepost.com/submissions/23955-hylian-transliterator',
	'http://hackuci.challengepost.com/submissions/23957-hellovr',
	'http://hackuci.challengepost.com/submissions/23958-pulley',
	'http://hackuci.challengepost.com/submissions/23959-horoscoper',
	'http://hackuci.challengepost.com/submissions/23963-immersive',
	'http://hackuci.challengepost.com/submissions/23964-trendit',
	'http://hackuci.challengepost.com/submissions/23965-creamy-chemistry',
	'http://hackuci.challengepost.com/submissions/23966-one-decision',
	'http://hackuci.challengepost.com/submissions/23967-sitcom-simulator',
	'http://hackuci.challengepost.com/submissions/23968-youtube-visualizer',
	'http://hackuci.challengepost.com/submissions/23969-weigh20',
	'http://hackuci.challengepost.com/submissions/23970-quantalk',
	'http://hackuci.challengepost.com/submissions/23971-the-matrix',
	'http://hackuci.challengepost.com/submissions/23972-bridge',
	'http://hackuci.challengepost.com/submissions/23973-courseplannr',
	'http://hackuci.challengepost.com/submissions/23974-email-text-to-playlist',
	'http://hackuci.challengepost.com/submissions/23975-fast-food-runner',
	'http://hackuci.challengepost.com/submissions/23976-tatami-galaxies',
	'http://hackuci.challengepost.com/submissions/23977-parcel-app',
	'http://hackuci.challengepost.com/submissions/23978-ontime-alarm',
	'http://hackuci.challengepost.com/submissions/23979-rare-positivity-page',
	'http://hackuci.challengepost.com/submissions/23980-restaurantzz',
	'http://hackuci.challengepost.com/submissions/23981-organicontact',
	'http://hackuci.challengepost.com/submissions/23982-pytransaction',
	'http://hackuci.challengepost.com/submissions/23983-nobody-cares',
	'http://hackuci.challengepost.com/submissions/23984-stand-walk-drive',
	'http://hackuci.challengepost.com/submissions/23985-clique',
	'http://hackuci.challengepost.com/submissions/23986-alonso',
	'http://hackuci.challengepost.com/submissions/23987-shark-education',
	'http://hackuci.challengepost.com/submissions/23988-sleep-maze',
	'http://hackuci.challengepost.com/submissions/23989-lynker',
	'http://hackuci.challengepost.com/submissions/23990-mobimouse',
	'http://hackuci.challengepost.com/submissions/23991-assassin-s-hitlist',
	'http://hackuci.challengepost.com/submissions/23992-pantry',
	'http://hackuci.challengepost.com/submissions/23993-findr',
	'http://hackuci.challengepost.com/submissions/23994-blindbound',
	'http://hackuci.challengepost.com/submissions/23995-tipsy',
	'http://hackuci.challengepost.com/submissions/23996-zany-balls',
	'http://hackuci.challengepost.com/submissions/23997-emotionall',
	'http://hackuci.challengepost.com/submissions/23998-frugalfriends',
	'http://hackuci.challengepost.com/submissions/23999-mood-music',
	'http://hackuci.challengepost.com/submissions/24000-which',
	'http://hackuci.challengepost.com/submissions/24001-phworld',
	'http://hackuci.challengepost.com/submissions/24002-droidpass',
	'http://hackuci.challengepost.com/submissions/24003-save-a-space'
];

count = {};

for url in urls:
	
	print('==================================================')
	print("Parsing: ", url)
	print('==================================================')
	

	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	response.code
	html = response.read()
	dom = BeautifulSoup(html)

	## find tags
	# platform = dom.find('div', {
		# 'class' : 'bloc submission-platforms submission-label-list clearfix'
	# })
	# platformTags = platform.find_all('li');
	
	# for tag in platformTags:
		# print(tag.span.a.string)
		
	tags = dom.find_all('span', {
		'class' : 'cp-tag recognized-tag'
	})
	
	for tag in tags:
		key = str(tag.a.string)
		if key in count:
			count[key] += 1
		else:
			count[key] = 1
		

	for key in sorted(count.keys()):
		print(key, ": ", count[key])
		
