from BaseClasses import Location

class ArchipIDLELocation(Location):
    game: str = "ArchipIDLE"

location_table = {}
start_id = 9000
for i in range(1, 201):
    location_table[f"IDLE item number {i}"] = start_id
    start_id += 1
