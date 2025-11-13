import os
import numpy as np
from flask import Flask, request, jsonify
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import io

app = Flask(__name__)

model = None

# Helper Function
def load_kmodel():
    global model    
    model_path = os.getenv("MODEL_PATH", "best_model.h5")
    try:
        model = load_model(model_path, compile=False)        
        model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    except Exception as e:
        print(f"Error loading model: {e}")
        raise
        
# Helper Function
def preprocess_image(img):
    img = img.convert("RGB")            
    img = img.resize((128, 128))        
    img_array = np.array(img).astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)  
    return img_array

# GET Request
@app.route('/summary', methods=['GET'])
def summary():
    global model
    if model is None:
        load_kmodel()
    info = {
        "model_name": "Alternate-LeNet5",
        "description": "Classify images predicting whether the building has been damaged by a hurricane",
        "input_shape": list(model.input_shape),
        "output_shape": list(model.output_shape),
        "number_of_parameters": model.count_params()
    }
    
    return jsonify(info)

# POST Request
@app.route('/inference', methods=['POST'])
def inference():
    global model
    if model is None:
        load_kmodel()

    file = None
    if 'file' in request.files:
        file = request.files['file']
    elif 'image' in request.files:
        file = request.files['image']
    elif request.data:
        file = io.BytesIO(request.data)
    else:
        return jsonify({"error": "No image provided"}), 400

    img = Image.open(file)
    processed = preprocess_image(img)
    preds = model.predict(processed)

    if len(preds.shape) == 2 and preds.shape[1] == 1:
        probability = float(preds[0, 0]) 
        if probability >= 0.5:
            cls = 1
        else:
            cls = 0
    else:
        cls = int(np.argmax(preds, axis=1)[0])

    label = "damage" if cls == 0 else "no_damage"
    return jsonify({"prediction": label}), 200


if __name__ == '__main__':
    load_kmodel()
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
