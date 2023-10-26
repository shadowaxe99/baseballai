```python
import plotly.graph_objects as go
from backend.data_processing import fetchData

def createInteractiveVisualizations():
    data = fetchData()

    # Performance Analytics Visualization
    fig1 = go.Figure(data=[
        go.Bar(name='Spin Efficiency', x=data['player'], y=data['spin_efficiency']),
        go.Bar(name='Hard-Hit Rate', x=data['player'], y=data['hard_hit_rate'])
    ])
    fig1.update_layout(barmode='group', title_text='Performance Analytics')
    fig1.show()

    # Scouting Reports Visualization
    fig2 = go.Figure(data=[
        go.Scatter(name='Recent Performances', x=data['date'], y=data['performance'], mode='lines+markers')
    ])
    fig2.update_layout(title_text='Scouting Reports')
    fig2.show()

    # AI-driven Insights Visualization
    fig3 = go.Figure(data=[
        go.Scatter(name='Predicted Performance', x=data['date'], y=data['predicted_performance'], mode='lines+markers')
    ])
    fig3.update_layout(title_text='AI-driven Insights')
    fig3.show()

createInteractiveVisualizations()
```