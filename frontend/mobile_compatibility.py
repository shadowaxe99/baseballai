```python
from flask import Flask, render_template
from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template

app = Flask(__name__)
Mobility(app)

@app.route('/')
@mobile_template('{mobile/}index.html')
def index(template):
    return render_template(template)

if __name__ == '__main__':
    app.run(debug=True)
```
This Python code uses Flask and Flask-Mobility to create a simple web application that serves different templates based on whether the user is on a mobile device or not. The `@mobile_template` decorator is used to specify a different template for mobile users. In this case, if a user accesses the site from a mobile device, the `mobile/index.html` template will be used.