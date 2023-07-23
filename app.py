# Objetivo - Criar uma api que permita a criação, consulta, edição, ou exclusão de músicas.
# URL base - localhost
# Endpoints -
    # localhos/songs (GET)
    # localhos/songs (POST)
    # localhost/songs/id (GET)
    # localhost/songs/id (PUT)
    # localhos/songs/id (DELETE)

# Recursos - Músicas

from flask import Flask, jsonify, request

app = Flask(__name__)

songs = [
    {
        'id': 1,
        'title': 'TNT',
        'artist': 'AC/DC'
    },
    {
        'id': 2,
        'title': 'Fear of the Dark',
        'artist': 'Iron Maiden'
    },
    {
        'id': 3,
        'title': 'Love Gun',
        'artist': 'Kiss'
    },
    {
        'id': 4,
        'title': 'Killing in the name',
        'artist': 'Rage Against the Machine'
    },
    {
        'id': 5,
        'title': 'Raining Blood',
        'artist': 'Slayer'
    }
]

# Consultar(geral)
@app.route('/songs', methods=['GET'])
def get_songs():
    return jsonify(songs)

# Consultar(id)
@app.route('/songs/<int:id>', methods=['GET'])
def get_songs_by_id(id):
    for song in songs:
        if song.get('id') == id:
            return jsonify(song)
        
# Editar
@app.route('/songs/<int:id>', methods=['PUT'])
def edit_sohg_by_id(id):
    att = request.get_json()
    for indice, song in enumerate(songs):
        if song['id'] == id:
            songs[indice].update(att)
            return jsonify(songs[indice])

# Excluir

app.run(port=5000, host='localhost', debug=True)