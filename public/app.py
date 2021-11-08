from flask import Flask, url_for, render_template, redirect
from forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json
from flask_wtf import FlaskForm

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'randomkey' 

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

@app.route('/', methods=('GET', 'POST'))

def startApp():
    form = PredictForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        # NOTE: Inserir token IAM:
        
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
                 + "<IAM_TOKEN>"}
                 

        if(form.genero.data == None): 
          python_object = []
        else:
          python_object = [form.bustotorax.data, form.quadril.data, float(form.cintura.data),
            form.genero.data]
        #Transforma objetos Python em JSON Files

        userInput = []
        userInput.append(python_object)

        # NOTE: array de valores para serem registrados
        payload_scoring = {"input_data": [{"fields": ["bustotorax", "quadril", "cintura",
          "genero"], "values": userInput }]}

        response_scoring = requests.post("<REQUEST_LINK>", json=payload_scoring, headers=header)

        output = json.loads(response_scoring.text)
        print(output)
        for key in output:
          ab = output[key]
        

        for key in ab[0]:
          bc = ab[0][key]
        
        roundedCharge = round(bc[0][0],2)

  
        # NOTE: Converte o valor númerico que representa os tamanhos para letras
        if (roundedCharge <=1): 
          form.abc= 'PP'

        elif (roundedCharge >1 and roundedCharge <=2): 
          form.abc= 'P'
        
        elif (roundedCharge >2 and roundedCharge <=3): 
          form.abc= 'M'
          
        elif (roundedCharge >3 and roundedCharge <=4): 
          form.abc= 'G' 
        
        elif (roundedCharge >4 and roundedCharge <=5): 
          form.abc= 'GG'
        
        elif (roundedCharge >5 and roundedCharge <=6): 
          form.abc= 'XGG'

        else:
          form.abc = 'Desculpe, algo deu errado. Tente novamente!' 

        return render_template('index.html', form=form)