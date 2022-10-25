names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

names = names + names1
new_names = []

guest_1 = input('Name of you personal guest member : ')
guest_2 = input('Name of you honor member : ')

names.append(guest_1)
names.append(guest_2)

for name in names :
    cap_names = []
    for i in name.split() :
        i.capitalize()
        cap_names.append(i.capitalize())
    # print(' '.join(cap_names))
    new_names.append(' '.join(cap_names))
    print(new_names)

for name in new_names :
    print(f'{name} --> you are invited to the party on Satursday!')