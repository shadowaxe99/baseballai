```python
from flask import Flask, render_template, request, redirect, url_for
from backend.authentication import login_required

app = Flask(__name__)

@app.route('/')
@login_required
def home():
    return render_template('dashboard.html')

@app.route('/performance-analytics')
@login_required
def performance_analytics():
    return render_template('performance_analytics.html')

@app.route('/scouting-reports')
@login_required
def scouting_reports():
    return render_template('scouting_reports.html')

@app.route('/ai-insights')
@login_required
def ai_insights():
    return render_template('ai_insights.html')

@app.route('/data-collection')
@login_required
def data_collection():
    return render_template('data_collection.html')

if __name__ == '__main__':
    app.run(debug=True)
```