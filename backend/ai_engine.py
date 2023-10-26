```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

class AIEngine:
    def __init__(self, db):
        self.db = db
        self.model = None

    def load_data(self):
        query = "SELECT * FROM player_performance"
        data = pd.read_sql_query(query, self.db)
        return data

    def preprocess_data(self, data):
        data.dropna(inplace=True)
        y = data.Performance
        X = data.drop(['Performance'], axis=1)
        return train_test_split(X, y, test_size=0.2, random_state=0)

    def train_model(self, X_train, y_train):
        model = RandomForestRegressor(n_estimators=100, random_state=0)
        model.fit(X_train, y_train)
        self.model = model

    def evaluate_model(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        return mean_absolute_error(y_test, predictions)

    def predict_performance(self, player_data):
        return self.model.predict(player_data)

    def run(self):
        data = self.load_data()
        X_train, X_test, y_train, y_test = self.preprocess_data(data)
        self.train_model(X_train, y_train)
        mae = self.evaluate_model(X_test, y_test)
        print("Mean Absolute Error of the model is: ", mae)
```
This Python code for `backend/ai_engine.py` creates a class `AIEngine` that loads player performance data from a database, preprocesses the data, trains a Random Forest Regressor model on the data, evaluates the model, and makes predictions. The `run` method executes these steps in sequence. The database connection is passed to the `AIEngine` when it's instantiated. The model is stored as an instance variable for reuse in predictions.