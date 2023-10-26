```python
import requests
import json
from backend.database import Database

class APIIntegration:
    def __init__(self):
        self.db = Database()
        self.api_key = "YOUR_API_KEY"  # Replace with your actual API key
        self.base_url = "https://api.mysportsfeeds.com/v2.0/pull/mlb/"

    def fetch_data(self, endpoint):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(f"{self.base_url}{endpoint}", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def sync_data(self):
        # Fetch and sync player data
        player_data = self.fetch_data("players.json")
        if player_data:
            self.db.insert_players(player_data)

        # Fetch and sync game data
        game_data = self.fetch_data("games.json")
        if game_data:
            self.db.insert_games(game_data)

        # Fetch and sync performance data
        performance_data = self.fetch_data("player_gamelogs.json")
        if performance_data:
            self.db.insert_performances(performance_data)

if __name__ == "__main__":
    api_integration = APIIntegration()
    api_integration.sync_data()
```