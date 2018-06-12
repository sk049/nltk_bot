from flask import Flask, render_template,request
import requests
app = Flask(__name__)


@app.route('/')
def chatbot():
   return render_template('chatBotPage.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print(userText)
    url = 'http://127.0.0.1:5002/initiate_chat'
    data = {"message": userText}
    res=requests.post(url, data=data)
    print(res)
    return res

 

if __name__ == '__main__':
   app.run(debug = True)