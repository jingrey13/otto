import requests
token="415048379:AAHoccZk9RPZll17K2mroxTp3U7qMl9s3sg"

class BotHandler:
  
  def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
  def send_message(self, chat_id, text):
			params = {'chat_id': chat_id, 'text': text}
			method = 'sendMessage'
			resp = requests.post(self.api_url + method, params)
			return resp
    
mybot = BotHandler(token)
mybot.send_message(114698280, 'Hello123')
