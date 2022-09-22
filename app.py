from chatbot_model import chatbot_response
from textblob import TextBlob

check_wikipedia1 = ['what', 'is']
check_wikipedia2 = ['who', 'is']
check_wikihow = ['how', 'to']


def get_bot_response():
    user_request = user_request.lower()

    print("Input: ", user_request, type(user_request))

    user_request = str(user_request)
    blob = TextBlob(user_request)
    usr_lang = blob.detect_language()
    print(usr_lang)
    if usr_lang == "en":
        response = chatbot_response(user_request)
        return response
