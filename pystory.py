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
model="gpt-3.5-turbo"
# model="gpt-4"


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
    name = data.get('name', 'User')

    # initial = f"""
    # Tell me a choose your own adventure story. The story is set in a {genre} universe. The main character's name is {name}. The genre is comedy and adventure. Make the story captivating. Give me multiple choices. Your response must have the following JSON structure: 
    # `{{
    #     "story": "Story content...",
    #     "options": [
    #         {{
    #             "A": "text for option A"
    #         }},
    #         {{
    #             "n": "text for option n"
    #         }}
    #     ],
    # }}` 
    # Start the story and ask the first question.
    # """


    initial = f"""
    Act as a choose your own adventure story teller. The story must contain these important attributes:
    Engaging Narrative: The story should be intriguing and engaging to keep the reader interested.
    The story is set in a {genre} universe. 
    Choice Points: These are the decision-making moments where the reader has to select one of multiple paths. The narrative should naturally lead to these points and offer compelling options.
    Branching Paths: The narrative branches off in different directions based on the choices made by the reader. Each branch should offer a distinct narrative pathway, ensuring readers feel their choices have significant consequences.
    Multiple Endings: The story must offer multiple endings. Depending on the choices made, the reader should be able to reach different conclusions. Some endings might be "better" than others, but all should be satisfying and coherent.
    Replayability: The story should be designed in a way that encourages readers to explore different paths. This means making sure that even "wrong" choices or "bad" endings offer some kind of narrative payoff, so readers are incentivized to replay the story.
    Balance: While choices should have consequences, you need to balance this against the reader's ability to complete the story. If all paths but one lead to a premature end, readers may get frustrated. Similarly, if choices don't really matter and all paths lead to the same end, readers may feel cheated.
    Clarity: Your reader should be able to easily understand the choices they're making. Avoid vague or misleading choices, as these can lead to frustration. It should also be clear to the reader when they've reached an ending and how to start a new path.
    Character Development: Even though the story's focus is on its branching paths, don't forget about character development. The main character(s) should be dynamic and relatable to ensure reader investment in their journey.
    The protagonist's name is {name}. 
    Your response must have the following JSON structure: 
    `{{
        "story": "Story content...",
        "options": [
            {{
                "A": "text for option A"
            }},
            {{
                "n": "text for option n"
            }}
        ],
    }}` 
    Start the story and ask the first question.
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
