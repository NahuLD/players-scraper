import requests
import random

base_url = 'https://api.namemc.com/profile/{}/friends'

file = open('player-list.txt', 'w+')

# we will assume that the first profile used will have a friend list
def runner(kicker, characters):
	known = []
	next = kicker
	while(True):
		names, uuids = parse_user(next)
		for index in range(len(uuids)):
			name = names[index]
			if len(name) > characters:
				continue
			
			uuid = uuids[index]
			if uuid in known:
				print('User is on list, skipping...')
				continue
			known.append(uuid)
			file.write('{},{}\n'.format(name, uuid))
			print('Added "{}" to the list'.format(name))
		
		print('List is now composed of', len(known), 'users!')
		key = input('Press (c) to continue and any other key to stop: ')
		if key != 'c':
			break
		
		next = get_next_user(uuids)
		if next is None:
			print('No user suitable found, stopping program...')
			break
	file.close()
	print('Stopped working, all results saved in "players.txt".')

def get_next_user(uuids):
	next = None
	while (True):
		possible = random.choice(uuids)
		if not check_user(possible):
			continue
		next = possible
		break
	return next

def parse_user(user):
	request = requests.get(base_url.format(user))
	names, uuids = [], []
	for item in request.json():
		names.append(item['name'])
		uuids.append(item['uuid'])
	return names, uuids

def check_user(uuid):
	request = requests.get(base_url.format(uuid))
	return len(request.json()) > 0

kicker = input('Please input a suitable user: ')
characters = int(input('Max amount of characters in the name: '))
runner(kicker, characters)
