from flask import Flask,request,jsonify , render_template
from flask_cors import CORS
import recommendation
import json
import os

app = Flask(__name__)
CORS(app) 


@app.route('/',methods =['GET','POST'])
def index():
    
    return render_template('index.html')

        
@app.route('/get_movie_list/',methods =['GET','POST'])
def recommend_movie_list():
    request.get_data()
    try:
        data = request.data
    except:
        try:
            data = request.json
        except:
            try:
                data = request.args
            except:
                data = request.form
    
    json_data = json.loads(data)
    print(json_data)
    movie_list = recommendation.results(json_data['input_movie'])
    if len(movie_list) ==1:
        return '',404
    else:
    
        return json.dumps({'recommanded_movies': movie_list})

if __name__=='__main__':
        port = int(os.environ.get('PORT', 5000))

        app.run(host= '0.0.0.0' ,port =port, debug = True)


