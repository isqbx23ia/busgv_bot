from aiogram import types

def register_start(dp):
    @dp.message_handler(commands=["start", "help"])
    async def send_welcome(message: types.Message):
        await message.reply(
            "Olá! Envie o número do ponto ou use /estimativas <ponto_id> para consultar horários.\n"
            "Use /buscarponto <nome> para encontrar pontos próximos."
        )