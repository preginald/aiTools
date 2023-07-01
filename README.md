# Flask Choose Your Own Adventure API

This is a Flask API that implements a choose your own adventure conversation using the OpenAI GPT-3.5 Turbo model. It allows you to create interactive story-like conversations where users can make choices and receive responses based on those choices.

## Prerequisites

Before running the application, make sure you have the following:

- Python 3.7 or higher installed
- OpenAI API key
- `.env` file containing the OpenAI API key (refer to `.env.example` for the required format)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/preginald/aiTools.git
cd aiTools.git
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Rename the `.env-example` file to `.env`.

```bash
mv .env-example .env
```

2. Open the `.env` file and replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.

```bash
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

## Usage

1. Start the Flask server:

```bash
python pystory.py
```
2. By default, the API will be accessible at `http://localhost:5000`. You can test it using a REST client or integrate it into your own applications.

## API Endpoints

### POST /api/conversation

Starts or continues a choose your own adventure conversation.

**Request Body:**

The request body must be in JSON format and include a `messages` array containing the conversation messages. Each message object should have a `role` and `content`.

Example:

```json
{
  "messages": [    {      "role": "system",      "content": "Tell me a choose your own adventure story..."    },    {      "role": "user",      "content": "Option A"    },    ...  ]
}
```

**Response:**

The API will respond with a JSON object containing the generated message content.

Example:
```json
{
  "message": "The generated message content..."
}
```
# Contributing
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License.