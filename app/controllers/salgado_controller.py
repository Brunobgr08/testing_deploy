from flask import request, current_app
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from werkzeug.exceptions import NotFound


from app.models.salgado_model import SalgadoModel


def criar_salgado():
    data = request.get_json()

    salgado = SalgadoModel(**data)

    current_app.db.session.add(salgado)
    current_app.db.session.commit()

    return {
        "id": salgado.id,
        "nome": salgado.nome,
        "preco": salgado.preco,
    }

def criar_multiplos_salgados():
    data = request.get_json()

    salgados = [SalgadoModel(**salgado) for salgado in data["salgados"]]

    current_app.db.session.add_all(salgados)
    current_app.db.session.commit()

    return {
        "salgados": [
            {
                "id": salgado.id,
                "nome": salgado.nome,
                "preco": salgado.preco,
            } for salgado in salgados
        ]
    }

def pegar_salgados():
    salgados = (
        SalgadoModel
        .query
        .all()
    )

    serializer = [
        {
            "id": salgado.id,
            "nome": salgado.nome,
            "preco": salgado.preco,
        } for salgado in salgados
    ]

    return {"salgados": serializer}

def salgados_por_id(salgado_id):
    salgado = (
        SalgadoModel
        .query
        .get(salgado_id)
    )

    return {
        "id": salgado.id,
        "nome": salgado.nome,
        "preco": salgado.preco
    }

def primeiro_salgado():
    salgado = (
      SalgadoModel
      .query.first()
    )

    return {
      "id": salgado.id,
      "nome": salgado.nome,
      "preco": salgado.preco
    }

def filtro(salgado_nome):
    salgado = (
      SalgadoModel
      .query
      .filter(SalgadoModel.nome==salgado_nome)
      .first()
    )

    return {
      "id": salgado.id,
      "nome": salgado.nome,
      "preco": salgado.preco
    }

def filtro2(salgado_nome):
    salgado = (
      SalgadoModel
      .query
      .filter_by(nome=salgado_nome)
      .first()
    )

    return {
      "id": salgado.id,
      "nome": salgado.nome,
      "preco": salgado.preco
    }

# def um_salgado(salgado_preco):
#     try:
#         salgado = SalgadoModel.query.filter_by(preco=salgado_preco).one()
#         ...
#     except (NoResultFound, MultipleResultsFound):
#         ...

# def um_salgado_ou_nenhum(salgado_preco):
#     try:
#         salgado = (
#             SalgadoModel
#             .query
#             .filter_by(preco=salgado_preco)
#             .one_or_none()
#         )
#         ...
#     except MultipleResultsFound:
#         ...

# def primeiro_ou_404(salgado_nome):
#     try:
#         salgado = (
#           SalgadoModel
#           .query
#           .filter_by(nome=salgado_nome)
#           .first_or_404(description="Salgado não encontrado")
#         )
#         ...
#     except NotFound as e:
#         ...

# def pegar_ou_404(salgado_id):
#     try:
#       salgado = (
#           SalgadoModel
#           .query
#           .get_or_404(salgado_id, description="Salgado não encontrado")
#       )
#       ...

#     except NotFound as e:
#         ...