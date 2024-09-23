import json

def extract_text(image):
    text = predict_step(image)
    result = {"extracted_text": text}
    return json.dumps(result)