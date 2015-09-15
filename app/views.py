from flask import Flask
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
        """Register new member"""
        return {}

    def delete(self):
        """

        :return:
        """
        return {}





#routes
api.add_resource(Members, '/')

