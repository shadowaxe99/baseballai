```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from database import Database

class DataProcessing:
    def __init__(self):
        self.db = Database()

    def fetch_data(self):
        query = "SELECT * FROM player_performance"
        data = self.db.execute_query(query)
        return data

    def clean_data(self, data):
        data.dropna(inplace=True)
        return data

    def transform_data(self, data):
        numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
        scaler = StandardScaler()
        data[numerical_features] = scaler.fit_transform(data[numerical_features])
        return data

    def process_data(self):
        raw_data = self.fetch_data()
        clean_data = self.clean_data(raw_data)
        transformed_data = self.transform_data(clean_data)
        return transformed_data

if __name__ == "__main__":
    dp = DataProcessing()
    processed_data = dp.process_data()
    print(processed_data.head())
```