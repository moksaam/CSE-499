from flask import Flask, jsonify, request, session
from mydb import db
from user.models import User
import uuid

class playerCharacter:

    def saveChar(self):
        print(request.form)

        if 'user' in session:
            user_id = session['_id']
            print(user_id)
            

        # Create the player character object
        pCharacter = {            
            "_id": uuid.uuid4().hex,
            "user_id": session['_id'],
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

        if db.characters.insert_one(pCharacter):
            return jsonify(pCharacter), 200