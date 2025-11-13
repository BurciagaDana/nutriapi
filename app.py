from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Asegúrate de usar tu propia clave API
API_KEY = "TU_API_KEY_AQUI"  # Reemplaza con tu clave real

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
            "addRecipeInformation": True  # Agrega más información como ingredientes, etc.
        }

        # Realiza la solicitud a Spoonacular
        response = requests.get(url, params=params)

        # Si la respuesta es exitosa, obtén las recetas
        if response.status_code == 200:
            data = response.json()
            recetas = data.get("results", [])
        else:
            recetas = []
    
    return render_template("index.html", recetas=recetas, query=query)

if __name__ == "__main__":
    app.run(debug=True)
