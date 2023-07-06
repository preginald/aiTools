from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv
import logging

# Set up logging configuration
logging.basicConfig(filename='app.log', level=logging.DEBUG)

app = Flask(__name__)
# CORS(app)  # This will enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
# model="gpt-3.5-turbo"
model="gpt-4"


load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']


# initial = "Tell me something random"

@app.route('/api/conversation', methods=['POST'])
def converse():
    variable = 'Your variable'
    app.logger.debug(variable)  
    data = request.get_json(force=True)
    messages = data['messages']

    # Include the user's selected genre and name in the initial prompt
    genre = data.get('genre', 'fantasy')
    # name = data.get('name', 'User')

    json_structure = """
    {
        "story": "Story content...",
        "options": [
            {
                "A": "text for option A"
            },
            {
                "n": "text for option n"
            }
        ]
    }
    """

    initial = f"""
    Create a compelling story. The genre is {genre}. The narrative should be engaging, offering multiple decision points leading to distinct and coherent conclusions. 

    Respond in the following JSON structure: 
    `{json_structure}`

    Begin the story and pose the first question.
    """

    # Ensure that the conversation starts with the system message
    if len(messages) == 0 or messages[0]['role'] != 'system':
        messages.insert(0, {"role": "system", "content": initial})

    try:
        completion = openai.ChatCompletion.create(model=model, messages=messages)

        # Assuming completion.choices[0].message.content is in the required format as a string
        message_content = completion.choices[0].message.content
        # Removing newline characters and unnecessary spaces
        message_content = message_content.replace("\n", "").replace("    ", "")
        
        return jsonify({
            'message': message_content
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5010)
