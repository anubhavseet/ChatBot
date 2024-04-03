from flask import Flask, request, jsonify
from nltk.chat.util import Chat, reflections
from flask_cors import CORS;


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",],
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",],
    ],
    [
        r"quit",
        ["Bye bye. It was nice talking to you. See you soon :)"],
    ],
    [
        r"(.*) symptoms of diabetes",
        ["Common symptoms of diabetes include frequent urination, feeling very thirsty, feeling very hungry - even though you are eating, extreme fatigue, blurry vision, cuts/bruises that are slow to heal, weight loss - even though you are eating more (Type 1), tingling, pain, or numbness in the hands/feet (Type 2). Please consult with a healthcare professional for advice.",],
    ],
    [
        r"how to prevent diabetes",
        ["Some ways to prevent diabetes include regular physical activity, eating plenty of fiber, opting for whole grains, losing extra weight, making healthier food choices, and not smoking. Please consult with a healthcare professional for advice.",],
    ],
    [
        r" risk factors for diabetes",
        ["Risk factors for diabetes can include overweight, age, family history, high blood pressure, abnormal cholesterol and triglyceride levels, and others. Type 2 diabetes also has risk factors like physical inactivity, race, and certain health problems such as high blood pressure. Please consult with a healthcare professional for advice.",],
    ],
]


def chatbot_response(text):
    chat = Chat(pairs, reflections)
    return chat.respond(text)

app = Flask(__name__)
app.config['CORS_ALLOW_HEADERS'] = 'Content-Type'
CORS(app)

@app.route('/api/chat', methods=['POST'])
def get_chat_response():
    user_text = request.json['text']
    response = chatbot_response(user_text)
    return jsonify({'message': response})

if __name__ == "__main__":
    app.run(debug=True,port=5000)


