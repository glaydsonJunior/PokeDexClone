from flask import Flask, request, render_template, url_for
from pookemon import Poketest
app = Flask(__name__)

@app.route('/pokedex/', methods=['POST','GET'])
def index():
    try:
        if request.method == 'POST':
            pokemon_search = request.form['pokename']
            classe_poke = Poketest(pokemon_search)
            poke_image = classe_poke.art_work
            poke_id = classe_poke.pokemon_id
            poke_peso = classe_poke.pokemon_peso
            poke_altura = classe_poke.pokemon_altura
            poke_tipos = classe_poke.pokemon_tipos
            return render_template('pokedex.html', poke_image=poke_image, poke_id=poke_id, poke_peso=poke_peso,poke_altura=poke_altura, poke_tipos=poke_tipos)
        else:
            return render_template('pokedex.html')
    except:
        return render_template('errormsg.html')

if __name__ == '__main__':
    app.run(debug=True)
