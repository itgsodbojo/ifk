from flask import Flask, request
from flask.ext.restful import Resource, Api

from pony.orm import db_session


# import our app
from app import app
#import our models
from app.models import Member


# create the api (restful)
api = Api(app)



class Members(Resource):

    def get(self):
        """List of all members"""

        with db_session:

            return {

               member.id: {
                    'name': member.name,
                    'phpne':member.phone
                }
                for member in Member.select()  # 2


            }

    def put(self):
        """Register new member

            payload {"name":"joe doe","phone":"12345"}'


            example in curl:
            curl -X PUT  -d '{"name":"joe doe","phone":"12345"}' 127.0.0.1:5000 -H 'Content-Type: application/json'

            example in httpie:
            http PUT 127.0.0.1:5000  name='joe doe' phone=12345



        """

        data = request.json

        with db_session:
            member=Member(name=data['name'],phone=data['phone'])

        return {},200

    def delete(self):
        """

        :return:
        """



        return '', 204







#routes
api.add_resource(Members, '/')

