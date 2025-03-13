turniej_fifa/
│── index.html  (Główna strona turnieju)
│── style.css  (Stylizacja strony)
│── script.js  (Obsługa losowania i wyników)
│── server.py  (Backend – Flask dla losowania i tabeli)
│── static/
│   ├── logo.png  (Logo turnieju, jeśli chcesz)
│   ├── uploads/  (Folder na przesłane zdjęcia)
│── templates/
│   ├── ranking.html (Edycja rankingu)
│   ├── matches.html (Lista meczów)
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Turniej FIFA – System Szwajcarski</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Turniej FIFA – System Szwajcarski</h1>
    
    <form id="playerForm">
        <input type="text" id="playerName" placeholder="Dodaj gracza" required>
        <input type="number" id="playerRanking" placeholder="Ranking" required>
        <button type="submit">Dodaj</button>
    </form>

    <h2>Lista graczy</h2>
    <ul id="playerList"></ul>

    <button id="startTournament">Rozpocznij losowanie</button>

    <h2>Wyniki</h2>
    <div id="matches"></div>

    <script src="script.js"></script>
</body>
</html>
body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #1d1d1d;
    color: white;
}

h1, h2 {
    color: #feca57;
}

input, button {
    margin: 10px;
    padding: 10px;
}

button {
    background-color: #ff6b6b;
    color: white;
    border: none;
    cursor: pointer;
}
document.getElementById("playerForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let name = document.getElementById("playerName").value;
    let ranking = document.getElementById("playerRanking").value;

    let playerList = document.getElementById("playerList");
    let li = document.createElement("li");
    li.textContent = name + " (Ranking: " + ranking + ")";
    playerList.appendChild(li);

    document.getElementById("playerName").value = "";
    document.getElementById("playerRanking").value = "";
});

document.getElementById("startTournament").addEventListener("click", function() {
    alert("Losowanie rozpoczęte! (Tu dodamy system szwajcarski)");
});
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

players = []
matches = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_player", methods=["POST"])
def add_player():
    data = request.json
    players.append({"name": data["name"], "ranking": int(data["ranking"])})
    return jsonify({"status": "ok", "players": players})

@app.route("/start_tournament", methods=["POST"])
def start_tournament():
    players.sort(key=lambda x: x["ranking"], reverse=True)  # Sortowanie po rankingu
    global matches
    matches = [(players[i]["name"], players[i+1]["name"]) for i in range(0, len(players)-1, 2)]
    return jsonify({"matches": matches})

if __name__ == "__main__":
    app.run(debug=True)
