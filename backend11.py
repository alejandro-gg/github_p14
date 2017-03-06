# -*- coding: utf-8 -*-
print('didnt crash... good')

from flask import Flask, request, render_template, jsonify
import requests
import io
app = Flask(__name__)




with open('fetchthis.txt', 'r') as my_file:
    my_imported_data = my_file.read()


def process_api_data(nombreartista):
    miheaders = {
    **my_imported_data,
    'redirect_uri' : 'http://127.0.0.1:5000/api/artista/'
    }
    respuesta = requests.get('https://api.spotify.com/v1/tracks/' + nombreartista, headers=miheaders)
    respuesta = respuesta.json()
    return render_template('api_artista.html', **respuesta)
@app.route('/api/artista/<nombreartista>')
def api_artista(nombreartista):
    catches_result = process_api_data(nombreartista)
    return catches_result


with open('fetchthis_issac.txt', 'r') as my_file2:
    my_headers2 = {}
    for eachiter in my_file2:
        a, b = eachiter.split(',')
        b = b.strip('\n')
        my_headers2[a] = b
print('=======================a ver si es cierto')
print('=======================a ver si es cierto')
print('=====================a ver si es cierto')
print(my_headers2)
print(type(my_headers2))


@app.route("/api/lookup/<id>")
def get_id(id):
    params = get_params_for_id(id)
    return params
def get_params_for_id(id):
    response = requests.get("https://api.spotify.com/v1/tracks/" + id, headers = my_headers2)
    response = response.json()
    print('====================== below is the variable response')
    print('====================== below is the variable response')
    print('====================== below is the variable response')
    print(response)
    return render_template("artista_issac.html", **response)


@app.route('/home_backend11')
def home_backend11():
    return render_template('home_backend11.html')







if __name__ == '__main__':
    app.run(debug = True)
