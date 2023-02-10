import random

base_factions = [ 'The Arborec', 'The Barony of Letnev', 'The Clan of Saar', 'The Embers of Muaat', 'The Emirates of Hacan', 'The Federation of Sol', 'The Ghosts of Creuss', 'The L1Z1X Mindnet', 'The Mentak Coalition', 'The Naalu Collective', 'The Nekro Virus', 'Sardakk N’orr', 'The Universities of Jol-Nar', 'The Winnu', 'The Xxcha Kingdom', 'The Yin Brotherhood', 'The Yssaril Tribes']
pok_factions = [ 'The Argent Flight', 'The Empyrean', 'The Mahact Gene-Sorcerers', 'The Naaz-Rokha Alliance', 'The Nomad', 'The Titans of Ul', 'The Vuil’Raith Cabal']
omega_factions = ['The Council Keleres']

factions = []
while not factions:
    pok = input('Include Phrophecy of Kings factions? (Y/n): ').lower().strip() or 'y'
    if pok[0] == 'y':
        factions = base_factions + pok_factions
    elif pok[0] == 'n':
        factions = base_factions
while True:
    include_omega = input('Include Omega Codex Factions? (Y/n): ').lower().strip() or 'y'
    if include_omega[0] == 'y':
        factions += omega_factions
        break
    elif include_omega[0] == 'n':
        break


while(True):
    num_players = input('Enter number of players: ')
    if num_players.isdecimal():
        num_players = int(num_players)
        break

players = []
for x in range(1,num_players+1):
    name = f'P{x}'
    name = input(f'Enter name for player {x} (P{x}): ') or name
    players.append(name)

seed = int(random.random() * 1000)
seed = input(f'Enter a seed for the generator (default: {seed}): ') or seed
random.seed(seed)
random.shuffle(factions)

num_options = len(factions) // num_players
options = []
for i in range(num_players):
    options.append(factions[i*num_options:(i+1)*num_options])

for i in range(num_players):
    print(f'{players[i]}:\t{options[i]}')

extra_options = factions[num_options * num_players:]
print(f'Extra:\t{extra_options}')

