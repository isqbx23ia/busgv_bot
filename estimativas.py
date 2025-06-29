from aiogram import types
from services.ceturb_api import obter_estimativas

def register_estimativas(dp):
    @dp.message_handler(commands=["estimativas"])
    async def estimativas_cmd(message: types.Message):
        try:
            ponto_id = int(message.get_args())
            resposta = await obter_estimativas(ponto_id)
            await message.reply(resposta)
        except Exception:
            await message.reply("Envie: /estimativas <número do ponto>")