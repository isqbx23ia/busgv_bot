import aiohttp
from config import CETURB_BASE_URL

async def obter_estimativas(ponto_id):
    url = f"{CETURB_BASE_URL}/PrevisaoSafe/obterEstimativasPorOrigem"
    payload = { "pontoDeOrigemId": ponto_id }
    headers = {"Content-Type": "application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as resp:
            if resp.status == 200:
                data = await resp.json()
                if "estimativas" in data and data["estimativas"]:
                    resposta = ""
                    for estimativa in data["estimativas"]:
                        linha = estimativa.get("linha", "??")
                        destino = estimativa.get("destino", "??")
                        tempo = estimativa.get("previsao", "??")
                        resposta += f"Linha {linha} | Destino: {destino} | Chega em: {tempo} min\n"
                    return resposta
                else:
                    return "Nenhuma estimativa encontrada para esse ponto."
            else:
                return "Erro ao consultar a API da CETURB."