from flask import Flask, render_template, request, jsonify
from recommendation import recommend_gear

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route to fetch recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    gear_name = request.form['gear_name']
    recommendations = recommend_gear(gear_name)
    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)




# # Create virtual environment
# python -m venv venv

# # Activate virtual environmentclear
# # For Windows
# venv\Scripts\activate
# # For Linux/macOS
# source venv/bin/activate

# # Install dependencies
# pip install -r requirements.txt
