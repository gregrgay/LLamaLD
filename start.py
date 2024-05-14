from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import base64
import requests


app = Flask(__name__)
client = OpenAI(base_url="http://localhost:8000/v1", api_key="sk-1234")

@app.route('/')

def index():
    return render_template('describeimage.html')

def get_as_base64(url):
    return base64.b64encode(requests.get(url).content).decode('utf-8')
    
@app.route('/process', methods=['POST'])

def process():    
    if request.json.get('base64Input'):    
        imgurl = request.json.get('base64Input')
    elif request.json.get('imgurl'): 
        print("Request Input:" , request.json.get('imgurl'))
        image_url = request.json.get('imgurl')
        imgurl = get_as_base64(image_url)

    imgprompt = request.json.get('imgprompt')

    response = client.chat.completions.create(
        model="gpt-5-vision-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{imgurl}"
                    },
                },
                {"type": "text", "text": imgprompt},
            ],
            
            }
        ],
        temperature=0.1,
        stream=True,
    )

    output = ""
   #print(response)
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            output += chunk.choices[0].delta.content
   
    #print(jsonify({'output': output}))
    return jsonify({'output': output})
if __name__ == '__main__':
    app.run(debug=True)