from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = "TU_API_KEY_AQUI" 

@app.route("/", methods=["GET", "POST"])
def index():
    recetas = []
    query = ""

    if request.method == "POST":
        query = request.form.get("query")
        url = "https://api.spoonacular.com/recipes/complexSearch"
        params = {
            "apiKey": API_KEY,
            "query": query,
            "number": 10,
            "addRecipeInformation": True  
        }

    
        response = requests.get(url, params=params)

    
        if response.status_code == 200:
            data = response.json()
            recetas = data.get("results", [])
        else:
            recetas = []
    
    return render_template("index.html", recetas=recetas, query=query)

if __name__ == "__main__":
    app.run(debug=True)
