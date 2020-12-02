from flask import Flask
from app import app
from user.models import User
from character.models import playerCharacter

@app.route('/createCharacter/saveChar', methods=['POST'])
def saveChar():
    return playerCharacter().saveChar()