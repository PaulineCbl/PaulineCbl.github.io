birth_dates = {"Proust": 1871, "Claude Simon": 1913, "Jaccottet": 1925, "Flaubert": 1821}

nineteenth_count = 0
twentieth_count = 0

for person, date in birth_dates.items():
    if date < 1900:
        nineteenth_count += 1
    else:
        twentieth_count += 1

print("There are " + str(nineteenth_count) + " 19th-c births " + " and " + str(twentieth_count) + " 20th-c. births in my collection.")
