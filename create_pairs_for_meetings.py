import lowest_least_used as llu

with open("participants.txt") as f:
    participants = [x.strip() for x in f.readlines()]

all_groups = llu.lowest_least_used(len(participants), 2)


week = 1
weekly_participants = set()
print("--------------")
print(f"Week {week}")
print("--------------")
week += 1
for group in all_groups[0].sequence:
    if group[0] in weekly_participants or group[1] in weekly_participants:
        print("--------------")
        print(f"Week {week}")
        print("--------------")
        week += 1
        weekly_participants = set()
    weekly_participants.add(group[0])
    weekly_participants.add(group[1])
    person_1 = participants[group[0] - 1]
    person_2 = participants[group[1] - 1]
    print(f"{person_1} - {person_2}")
