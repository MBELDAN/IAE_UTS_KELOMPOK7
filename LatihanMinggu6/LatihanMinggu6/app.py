from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/premierleague')
def premier():
    url = "https://premier-league-standings1.p.rapidapi.com/"

    headers = {
        "X-RapidAPI-Key": "f3ca8e13f4msh46de789c7f6234cp19f80ajsn1163e1927d50",
        "X-RapidAPI-Host": "premier-league-standings1.p.rapidapi.com"
    }




    response = requests.get(url, headers=headers)
    arkan = response.json()
    return render_template('premier.html', data=arkan)

@app.route('/playerinf')
def playerinfo():
    url = "https://premier-league-players1.p.rapidapi.com/players"

    headers = {
        "X-RapidAPI-Key": "f5bb208837msh45f400f3016e4f8p169667jsn3fac8033682a",
        "X-RapidAPI-Host": "premier-league-players1.p.rapidapi.com"
    }


    response = requests.get(url, headers=headers)
    beldan = response.json()
    return render_template('playerinf.html', data=beldan)




@app.route('/transferlist')
def transfer():
    url = "https://sportapi7.p.rapidapi.com/api/v1/transfer"

    headers = {
        "X-RapidAPI-Key": "eea92a9621mshbb5f39383ef16f2p147c78jsn3b2a2ac99577",
        "X-RapidAPI-Host": "sportapi7.p.rapidapi.com"
}

    response = requests.get(url, headers=headers)
    naufal = response.json()
    return render_template('transfer.html', data=naufal)


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')