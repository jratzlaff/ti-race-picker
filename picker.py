import random

base_factions = [ 'The Arborec', 'The Barony of Letnev', 'The Clan of Saar', 'The Embers of Muaat', 'The Emirates of Hacan', 'The Federation of Sol', 'The Ghosts of Creuss', 'The L1Z1X Mindnet', 'The Mentak Coalition', 'The Naalu Collective', 'The Nekro Virus', 'Sardakk N’orr', 'The Universities of Jol-Nar', 'The Winnu', 'The Xxcha Kingdom', 'The Yin Brotherhood', 'The Yssaril Tribes']
pok_factions = [ 'The Argent Flight', 'The Empyrean', 'The Mahact Gene-Sorcerers', 'The Naaz-Rokha Alliance', 'The Nomad', 'The Titans of Ul', 'The Vuil’Raith Cabal']

while(True):
    pok = input('Include Phrophecy of Kings factions? (y/n) ')

    if pok in ['y', 'Y', 'n', 'N']:
        if(pok == 'y' or pok == 'Y'):
            factions = base_factions + pok_factions
        else:
            factions = base_factions
        break

while(True):
    num_players = input('Enter number of players: ')

    if num_players.isdecimal():
        num_players = int(num_players)
        break

players = []
for x in range(num_players):
    player = input('Enter player {}: '.format(str(x + 1)))
    players.append(player)

random.seed(random.random() * 12345)
random.shuffle(factions)

num_options = len(factions) // num_players
options = []
for i in range(num_players):
    options.append(factions[i*num_options:(i+1)*num_options])

for i in range(num_players):
    print('{}:\t{}'.format(players[i], str(options[i])))

extra_options = factions[num_options * num_players:]
print('Extra:\t{}'.format(extra_options))