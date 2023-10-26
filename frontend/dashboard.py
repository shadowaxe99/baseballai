```python
from flask import Flask, render_template
from backend.database import get_player_data, get_game_data, get_performance_data

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    player_data = get_player_data()
    game_data = get_game_data()
    performance_data = get_performance_data()

    return render_template('dashboard.html', player_data=player_data, game_data=game_data, performance_data=performance_data)

if __name__ == '__main__':
    app.run(debug=True)
```

Please note that this is a basic Flask application serving a dashboard page. The actual data visualization would be handled on the frontend using a library like D3.js or Chart.js within the 'dashboard.html' template. The functions `get_player_data()`, `get_game_data()`, and `get_performance_data()` are placeholders for the actual functions that would interact with your database.