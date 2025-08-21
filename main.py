from fastapi import FastAPI

app = FastAPI()

# Example driver standings
driver_standings = [
    {"position": 2, "driver": "Max Verstappen", "team": "Red Bull", "points": 200},
    {"position": 1, "driver": "Lando Norris", "team": "McLaren", "points": 300},
    {"position": 3, "driver": "Charles Leclerc", "team": "Ferrari", "points": 150}
]

# Example team standings
team_standings = [
    {"position": 1, "team": "Red Bull", "points": 350},
    {"position": 2, "team": "McLaren", "points": 280},
    {"position": 3, "team": "Ferrari", "points": 271}
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
