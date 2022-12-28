import random
base_factions = [ 'The Arborec', 'The Barony of Letnev', 'The Clan of Saar', 'The Embers of Muaat', 'The Emirates of Hacan', 'The Federation of Sol', 'The Ghosts of Creuss', 'The L1Z1X Mindnet', 'The Mentak Coalition', 'The Naalu Collective', 'The Nekro Virus', 'Sardakk N’orr', 'The Universities of Jol-Nar', 'The Winnu', 'The Xxcha Kingdom', 'The Yin Brotherhood', 'The Yssaril Tribes']

pok_factions = [ 'The Argent Flight', 'The Empyrean', 'The Mahact Gene-Sorcerers', 'The Naaz-Rokha Alliance', 'The Nomad', 'The Titans of Ul', 'The Vuil’Raith Cabal']

factions = base_factions+pok_factions
players = ['Jacob', 'Marc', 'Alex', 'Sam', 'Carl',]
num_players = len(players)
num_options = len(factions)//num_players
#TODO random seed
random.seed(10162022)
random.shuffle(factions)
options = []
for i in range(num_players):
    options.append(factions[i*num_options:(i+1)*num_options])

for i in range(num_players):
    print("{}:\t{}".format(players[i], str(options[i])))


