from flask import Flask
from app import app
from user.models import User
from items.models import pItems

@app.route('/createCharacter/saveItems', methods=['POST'])
def saveItems():
    return pItems().saveItems()