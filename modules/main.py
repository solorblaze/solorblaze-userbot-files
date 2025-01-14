# Solorblaze developer
# Module scheme (json):
# {
#      "link": "https://raw.githubusercontent.com/solorblaze/solorblaze-userbot-files/main/modules/main.py"
# }


import pyrogram


class Module:
    def __init__(self):
        "Module init"

        self.name = "TestModule"
        self.command_name = "main"
        self.version = "0.1"
        self.developer = "solorblaze"
        self.help = "/test - Test"
    
    def module_loaded(self):
        "Method for loading a module"
    
    async def message_handler(self, message : pyrogram.types.Message, send_message, command : str, args : list(str)):
        """
        Message handler
        send_message(text, message) - async def, to send (or change the text of the message if it is the owner of the userbot), with automatic translation into the language that is selected
        """
        if command == "/test": # Command: /test or /test!main
            await send_message("<i>Test!</i>")
