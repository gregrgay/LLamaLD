from flask import Flask, render_template, request, jsonify, send_from_directory
from openai import OpenAI
import base64
import requests


app = Flask(__name__)
#Adjust the base_url to point to the OpenAI/LLama server, noting the api-key can be any value for the local LLama server, or set to the appropriate key if using a public OpenAI server (e.g. ChatGPT4)
client = OpenAI(base_url="http://localhost:8000/v1", api_key="sk-1234")

@app.route('/')
def index():
    return render_template('describeimage.html')

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images', filename)

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
        # Tempurature range 0 to 1, setting to 0.1 prompts a more focused and expected answer, while 0.8 encourages a more creative response.
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