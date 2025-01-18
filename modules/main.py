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

        # Database
        self.database = 0
    
    def module_loaded(self):
        "Method for loading a module"
    
    async def message_handler(self, message : pyrogram.types.Message, send_message, command : str, args : list[str], database : dict[]):
        """
        Message handler
        send_message(text, message) - async def, to send (or change the text of the message if it is the owner of the userbot), with automatic translation into the language that is selected
        command - Stores a command, for example: if the message text is “/test 1” then the command will be “/test”
        args - Stores the command arguments, for example: if the message text is "/test 1" then the command arguments will be ["1"]
        database - Stores JSON format. It was added to store variables in memory. You can change the variable using set_key
        """
        if command == "/test": # Command: /test or /test!main
            await send_message("<i>Test!</i>")

    #def set_key(self,
module = Module()
