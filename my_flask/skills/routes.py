from flask import Flask
from app import app
from user.models import User
from skills.models import pSkills

@app.route('/createCharacter/saveSkills', methods=['POST'])
def saveSkills():
    return pSkills().saveSkills()