import pyrogram, re


class Module:
    def __init__(self):
        "Module init"

        self.name = "Code"
        self.command_name = "code"
        self.version = "0.1"
        self.developer = "solorblaze"
        self.help = "/check_code - Check code"

    def module_loaded(self):
        "Method for loading a module"

    async def message_handler(self, message : pyrogram.types.Message, send_message, command : str, args : list[str]):
        if command == "/check_code":
            def is_only_english_letters(text):
                emoji_pattern = re.compile(
                    "["
                    "\U0001F600-\U0001F64F"
                    "\U0001F300-\U0001F5FF"
                    "\U0001F680-\U0001F6FF"
                    "\U0001F700-\U0001F77F"
                    "\U0001F780-\U0001F7FF"
                    "\U0001F800-\U0001F8FF"
                    "\U0001F900-\U0001F9FF"
                    "\U0001FA00-\U0001FAFF"
                    "\U00002700-\U000027BF"
                    "]+", 
                    flags=re.UNICODE)
                text = emoji_pattern.sub(r'', text)
                
                cleaned_text = re.sub(r'[^a-zA-Z ]', '', text)
                
                cleaned_text = cleaned_text.replace(" ", "")
                
                return bool(re.match(r'^[a-zA-Z]+$', cleaned_text))
            def check_syntax(code):
                try:
                    ast.parse(code)
                    return True
                except Exception: return False
            
            code = ' '.join(args)

            result = "✅"
            reason = ""
            
            if not code.__contains__("class Module:"):
                result = "❌"
                reason = "Class \"Module\" not found."
            
            if not code.__contains__("def module_loaded(self)"):
                result = "❌"
                reason = "Method \"module_loaded\" not found"
            
            if not code.__contains__("async def message_handler("):
                result = "❌"
                reason = "Method \"message_handler\" not found"
            
            if code.lower().__contains__("self.developer = \"solorblaze\""):
                result = "❌"
                reason = "The developer cannot be Solorblaze"
            
            if code.lower().__contains__("self.name = \"TestModule\""):
                result = "❌"
                reason = "The name cannot be TestModule"
            
            if not code.__contains__("await send_message"):
                result = "❌"
                reason = "Please use send_message."

            if not code.__contains__("command"):
                result = "❌"
                reason = "Please use variable command."

            if not is_only_english_letters():
                result = "❌"
                reason = "Please use only english."

            if ".text.split(" in code.replace(" ", ""):
                result = "❌"
                reason = "Please insert \"module = Module()\" at the end of the code."
            
            if not check_syntax(code):
                result = "❌"
                reason = "Syntax error."

            if reason != "":
                reason = f"\nReason: <code>{reason}</code>"

            await send_message(f"<i>Result: {result}{reason}")

module = Module()
