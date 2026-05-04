_sightings = [
    {
        "id": 1,
        "location": "Ningaloo Reef, Australia",
        "date": "2024-03-15",
        "size_meters": 9.5,
        "observer": "Dr. Marina Torres",
        "notes": "Massive juvenile feeding at surface. Classic polka-dot pattern clearly visible."
    },
    {
        "id": 2,
        "location": "Isla Holbox, Mexico",
        "date": "2024-05-22",
        "size_meters": 7.2,
        "observer": "Carlos Ruiz",
        "notes": "Group of 3 whale sharks spotted near plankton bloom!"
    },
    {
        "id": 3,
        "location": "Donsol Bay, Philippines",
        "date": "2024-02-10",
        "size_meters": 11.0,
        "observer": "Lena Park",
        "notes": "Largest individual seen this season. 11m estimated from boat."
    },
]
_next_id = 4

def get_all_sightings():
    return list(_sightings)

def add_sighting(location, date, size_meters, observer, notes=""):
    global _next_id
    sighting = {
        "id": _next_id,
        "location": location,
        "date": date,
        "size_meters": float(size_meters),
        "observer": observer,
        "notes": notes,
    }
    _sightings.append(sighting)
    _next_id += 1
    return sighting

def get_stats():
    if not _sightings:
        return {"count": 0, "avg_size": 0, "max_size": 0}
    sizes = [s["size_meters"] for s in _sightings]
    return {
        "count": len(_sightings),
        "avg_size": round(sum(sizes) / len(sizes), 1),
        "max_size": max(sizes),
    }