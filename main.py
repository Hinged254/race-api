from fastapi import FastAPI

app = FastAPI()

# Example driver standings
driver_standings = [
    {"position": 1, "driver": "Piastri", "team": "McLaren", "points": 284},
    {"position": 2, "driver": "Norris", "team": "McLaren", "points": 275},
    {"position": 3, "driver": "Verstappen", "team": "Red Bull", "points": 187},
    {"position": 4, "driver": "Russel", "team": "Mercedes", "points": 172},
    {"position": 5, "driver": "Charles Leclerc", "team": "Ferrari", "points": 151},
    {"position": 6, "driver": "Hamilton", "team": "Ferrari", "points": 109},
    {"position": 7, "driver": "Antonelli", "team": "Mercedes", "points": 64},
    {"position": 8, "driver": "Albon", "team": "Williams", "points": 54},
    {"position": 9, "driver": "Hulkenberg", "team": "Kick Sauber", "points": 37},
    {"position": 10, "driver": "Ocon", "team": "Haas", "points": 27},
    {"position": 11, "driver": "Alonso", "team": "Aston Martin", "points": 26},
    {"position": 12, "driver": "Stroll", "team": "Aston Martin", "points": 26},
    {"position": 13, "driver": "Hadjar", "team": "Racing Bulls", "points": 22},
    {"position": 14, "driver": "Gasly", "team": "Alpine", "points": 20},
    {"position": 15, "driver": "Lawson", "team": "Racing Bulls", "points": 20},
    {"position": 16, "driver": "Sainz", "team": "Williams", "points": 16},
    {"position": 17, "driver": "Bortoleto", "team": "Kick Sauber", "points": 14},
    {"position": 18, "driver": "Tsunoda", "team": "Red Bull", "points": 10},
    {"position": 19, "driver": "Bearman", "team": "Haas", "points": 8},
    {"position": 20, "driver": "Colapinto", "team": "Alpine", "points": 0},
    {"position": 21, "driver": "Doohan", "team": "Alpine", "points": 0},
]

# Example team standings
team_standings = [
    {"position": 1, "team": "Mclaren", "points": 559},
    {"position": 2, "team": "Ferrari", "points": 260},
    {"position": 3, "team": "Mercedes", "points": 236},
    {"position": 4, "team": "Red Bull", "points": 194},
    {"position": 5, "team": "Williams", "points": 70},
    {"position": 6, "team": "Aston Martin", "points": 52},
    {"position": 7, "team": "Kick Sauber", "points": 51},
    {"position": 8, "team": "Racing Bulls", "points": 45},
    {"position": 9, "team": "Haas", "points": 35},
    {"position": 10, "team": "Alpine", "points": 20}

]

@app.get("/")
def root():
    return {"message": "F1 API is running!"}

@app.get("/drivers")
def get_drivers():
    return {"drivers": driver_standings}

@app.get("/teams")
def get_teams():
    return {"teams": team_standings}
