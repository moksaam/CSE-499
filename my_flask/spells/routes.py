from flask import Flask
from app import app
from user.models import User
from spells.models import pSpells

@app.route('/createCharacter/saveSpells', methods=['POST'])
def saveSpells():
    return pSpells().saveSpells()