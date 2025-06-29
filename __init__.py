from .start import register_start
from .estimativas import register_estimativas
from .itinerario import register_itinerario
from .buscar_ponto import register_buscar_ponto
from .fallback import register_fallback

def register_handlers(dp):
    register_start(dp)
    register_estimativas(dp)
    register_itinerario(dp)
    register_buscar_ponto(dp)
    register_fallback(dp)