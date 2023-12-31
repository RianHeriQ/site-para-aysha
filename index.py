from flask import Flask, render_template
from datetime import datetime
from time import strftime, sleep

app = Flask(__name__)


@app.route("/")
def index():
  
  relogio = datetime.now()
  current_time = relogio.strftime('%H:%M:%S')
    
  dia_semana = pegar_dias_pt(relogio.weekday())
  data = relogio.strftime('%d/%m/%Y')
  hora = relogio.strftime('%H:%M:%S')
    
  return render_template("index.html", current_time=current_time, data=data, hora=hora, dia_semana=dia_semana)

def pegar_dias_pt(dia):
  dias_pt = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
  return dias_pt[dia]

    
if(__name__ == "__main__"):
  app.run(debug=True)