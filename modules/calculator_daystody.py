import pyrogram

def format_float(number: float) -> str:
    if number == int(number):
        return str(int(number))

class Module:
    def __init__(self):
        "Module init"

        self.name = "CalculatorModule"
        self.command_name = "main"
        self.version = "0.1"
        self.developer = "@daystody"
        self.help = "/cl - calculator"

    def module_loaded(self):
        "Method for loading a module"

    async def message_handler(self, message : pyrogram.types.Message, send_message, command : str, args : list[str]):
        if command == "/cl":
            try:
                    value = ' '.join(args)
                    result = eval(value)
                    formatted_result = format_float(result)
                    await send_message(f"<b>📠 Решение:</b> <code>{formatted_result}</code>")
            except Exception as e:
                await send_message(f"❗ Ошибка при подсчёте примера: {e}")

module = Module()