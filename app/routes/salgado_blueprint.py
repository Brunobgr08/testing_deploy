from flask import Blueprint
from app.controllers.salgado_controller import criar_salgado, criar_multiplos_salgados, pegar_salgados


bp_salgado = Blueprint("bp_salgado", __name__, url_prefix="/salgados")

bp_salgado.post("")(criar_salgado)
bp_salgado.post("/multiplos")(criar_multiplos_salgados)
bp_salgado.get("")(pegar_salgados)


