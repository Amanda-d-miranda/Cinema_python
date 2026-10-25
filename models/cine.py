#CINE REPRESETA A ENTIDADE CINE (CINEMA)
from uuid import uuid4

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID

from db import db

class cine(db.models):
    __tablename__ = 'cine'

    ID = db.column(
        UUID(as_uuid=True, 
        primary_key = True, # primeira chave
        default = uuid4 ) 
    )

    nome_filme = db.column(
        String(255),
        null = False
    )

    diretor_filme = db.column(
        String(255),
        nullable = False
    )

    description = db.Column(
        Text,
        nullable = False
    )

    filme_favorito = db.Column(
        db.Bollean,
        nullabe = False,
        default = False,
    )

    assistindo = db.column(
        db.Boolean,
        nullable = False,
        default = False
    )

    filmes_finalizados = db.column(
        db.Boolean,
        nullable = False,
        default = False
    )


def desc(self):
    return{
        'id': str(self.id),
        'nome_filme': self.nome_filme,
        'diretor_filme': self.diretor_filme,
        'description': self.description,
        'filme_favorito' : self.filme_favorito,
        'assistindo': self.assistindo,
        'filmes_finalizados' : self.filmes_finalizados
    }
