from flask import Flask, jsonify, request

app = Flask(__name__)
from animes import animes
@app.route('/ping')
def ping():
    return jsonify({"message":"pong"})
@app.route('/animes')
def getAnimes():
    return jsonify({"animes": animes, "message": "My anime fav list"})

@app.route('/animes/<string:anime_name>')
def getAnime(anime_name):
    animeFound =  [anime for anime in animes if anime['name']== anime_name]
    if(len(animeFound) > 0):
      return jsonify({"anime": animeFound[0]})
    return jsonify({"Message": "Anime not found"})
@app.route('/animes', methods=['POST'])
def addAnime():
    new_anime = {
        'name': request.json['name'],
        'autor': request.json['autor']
    }
    animes.append(new_anime)
    print(request.json)
    return jsonify({"Message":"Anime added succesfully!", "Animes":animes})
@app.route('/animes/<string:anime_name>', methods=['PUT'])
def editAnime(anime_name):
 animeFound = [anime for anime in animes if anime['name'] == anime_name]
 if(len(animeFound) > 0):
     animeFound[0]['name'] = request.json['name']
     animeFound[0]['autor'] = request.json['autor']
     return jsonify({
         "Message": "Anime Updated",
         "anime": animeFound[0]
     })
     return jsonify({"Message": "Anime not found"})
@app.route('/animes/<string:anime_name>', methods=['DELETE'])
def deleteAnime(anime_name):
   animeFound = [anime for anime in animes if anime['name'] == anime_name]
   if(len(animeFound) > 0):
       animes.remove(animeFound[0])
       return jsonify({
           "Message": "Delete anime",
           "Animes": animes
       })
       return jsonify({
           "Message": "Product not found"
       })
if __name__ == '__main__':
    app.run(debug=True, port=5000)