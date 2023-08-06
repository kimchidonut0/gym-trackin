from flask import Flask
from flask import request, jsonify, json

app = Flask(__name__)

fitness_history = [{'date': 'Mon', 'activity': 'walk, 30 min'}, 
                   {'date': 'Tues', 'activity': 'tennis, 60 min'}, 
                   {'date': 'Weds', 'activity': 'pullup, 30 min'}, 
                   {'date': 'Thurs', 'activity': 'run, 30 min'}]

@app.route('/', methods=['GET'])
def hello_world():
   # strin =  "\nusing gunicorn\n"
   # print(request.headers)
   welcom = 'Welcome! To the fitness logging page'
   return welcom

@app.route('/logs', methods=['GET'])
def returnAll():
   return jsonify({'Logs': fitness_history})
   
@app.route('/logs/<string:date>', methods=['GET'])
def showDailyLog(date):
   res = fitness_history[0]
   for index, jsonobj in enumerate(fitness_history):
      if jsonobj['date'] == date:
         res = fitness_history[index]
   return jsonify({'Logs': res})

@app.route('/logs', methods=['POST'])
def addLog():
   print('adding logs')
   print(request.data)
   try:
      new_log = json.loads(request.data)
   except:
      print('error processing json')
   fitness_history.append(new_log)
   return jsonify({'Logs': fitness_history})


if __name__ == '__main__':
   app.run()