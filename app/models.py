from app import db
from datetime import datetime

class Contato(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow())
    nome = db.Column(db.String, nullable=True)
    email = db.Column(b.String, nullable=True)
    assunto = db.Cplumn(b.String, nullable=True)
    mensagem = db.Column(b.String, nullable=True)