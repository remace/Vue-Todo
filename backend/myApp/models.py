from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging as lg
import json

from .views import app

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    visible = db.Column(db.Boolean)
    done = db.Column(db.Boolean)

    def __init__(self,title,description,visible,done):
        self.title = title
        self.description = description
        self.visible = visible
        self.done = done
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return f'{ "[x]" if self.done else "[ ]"}\t{self.id}: {self.title}\t{"visible" if self.visible else "invisible"}\tcreated: {self.created_at}\tupdated:{self.updated_at}'

    def update(self, **kwargs):
        print(kwargs['kwargs'])
        is_updated = False
        if 'title' in kwargs['kwargs']:
            print('title')
            self.title = kwargs['kwargs'].get('title')
            is_updated = True
        if 'description' in kwargs['kwargs']:
            self.description = kwargs['kwargs'].get('description')
            is_updated = True
        if 'visible' in kwargs['kwargs']:
            self.visible = kwargs['kwargs'].get('visible')
            is_updated = True
        if 'done' in kwargs['kwargs']:
            self.done = kwargs['kwargs'].get('done')
            is_updated = True
        if is_updated:
            updated_at = datetime.now()

def init_db():
    db.drop_all()
    db.create_all()

    db.session.add(Todo("test","description",True,True))
    db.session.add(Todo("test2", "description 2", True, True))

    db.session.commit()
    lg.warning('database initialized')