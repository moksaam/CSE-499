from flask import Flask, jsonify, request, session
from app import db
import uuid

class playerCharacter:

    def saveChar(self):

        # Create the player character object
        pCharacter = {            
            "_id": uuid.uuid4().hex,
            "user_id": session.get('user_id'),
            "charName": request.form.get('charName'),
            "charRace": request.form.get('charRace'),
            "charAge": request.form.get('charAge'),
            "charSex": request.form.get('charSex'),
            "charHeight": request.form.get('charHeight'),
            "charWeight": request.form.get('charWeight'),
            "strAtt": request.form.get('strAtt'),
            "dexAtt": request.form.get('dexAtt'),
            "conAtt": request.form.get('conAtt'),
            "intAtt": request.form.get('intAtt'),
            "wisAtt": request.form.get('wisAtt'),
            "chaAtt": request.form.get('chaAtt')
        }

        return jsonify(pCharacter), 200