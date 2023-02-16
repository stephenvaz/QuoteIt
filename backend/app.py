import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS
import random
import difflib
app = Flask(__name__)
CORS(app)

model = pickle.load(open('model/model.pkl', 'rb'))
df = pd.read_csv('scrape/data/output/format2.csv')
quote_all = df['quote'].tolist()

@app.route("/")
def home():
    return "<h1>Server is live</h1>"

@app.route('/predict',methods=['POST'])
def predict():
    print('hello')
    try:
        request_data = request.get_json()
    except Exception as er:
        print(er)
    print("data: ", request_data)
    close_match =  difflib.get_close_matches(request_data['quote'], quote_all)
    # print(close_match)
    close = close_match[0]
    id_of_quote = df[df['quote'] == close]['id'].values[0]
    similarity_score = list(enumerate(model[id_of_quote]))
    # print(similarity_score)
    sorted_sim_quote = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    print(sorted_sim_quote)
    return_list = []
    i = 0
    for quote in sorted_sim_quote:
        if(i == 0):
            i +=1
            continue
        id = quote[0]
        quote_from_id = df[df['id'] == id]['quote'].values[0]
        print(quote_from_id)
        
        if(i == 6):
            break
        i += 1
        return_list.append(quote_from_id)
        # except:
        #     pass
    
    return jsonify(return_list)

if __name__ == "__main__":
    app.run(debug = True)