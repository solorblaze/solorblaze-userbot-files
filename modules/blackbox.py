import pyrogram
import requests
import json


class Module:
    def __init__(self):
        "Module init"

        self.name = "BlackBox"
        self.command_name = "blackbox"
        self.version = "0.1"
        self.developer = "solorblaze"
        self.help = "/bb, /ai, /blackbox - Send request"
    
    def module_loaded(self):
        "Method for loading a module"
    
    async def message_handler(self, message : pyrogram.types.Message, send_message, command : str, args : list[str]):
        if ["/bb", "/ai", "/blackbox"] in command:
            requests_ = ' '.join(args)
            
            
            url = "https://api.blackbox.ai/api/chat"

            payload = json.dumps({
            "messages": [
                {
                "content": requests_,
                "role": "user"
                }
            ],
            "model": "BLACKBOX.AI",
            "max_tokens": "1024"
            })
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            await send_message(response.text)
module = Module()
