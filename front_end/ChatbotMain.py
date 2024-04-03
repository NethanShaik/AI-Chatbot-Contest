from flask import Flask, request, jsonify, render_template
import pandas as pd
import gensim
from gensim.parsing.preprocessing import preprocess_documents
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
app = Flask(__name__)
app.config["DEBUG"] = True

# Dummy model function for demonstration
def model_predict(input_data):
    # Your model's prediction logic goes here
    return {"result": "Model output based on " + str(input_data)}

@app.route('/')
def home():
    return render_template('/ChatbotHome.html')

@app.route('/model', methods=['POST'])
def handle_model():
    # Get data from the POST request
    data = request.json
    user_data=data['input']


    # Process the data and interact with the model
    df = pd.read_csv("wiki_movie_plots_deduped.csv", sep=",")
    df = df[df["Release Year"] >= 2000]
    model=Doc2Vec.load("doc2vec_model1.model")
    user_data = gensim.parsing.preprocessing.preprocess_string(user_data)
    test_doc_vector = model.infer_vector(user_data)
    sims = model.docvecs.most_similar(positive = [test_doc_vector])
    output = df['Title'].iloc[sims[0][0]]
    key='response'
    model_output={key:output}

    # Send the model's output back as a JSON response
    return jsonify(model_output)

if __name__ == '__main__':
    app.run(debug=True)





