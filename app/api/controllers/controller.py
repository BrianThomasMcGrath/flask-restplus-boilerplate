from flask import request
from flask_restplus import Resource, Namespace

from app.api.models import sample_request

sample = Namespace('sample', description="Sample api route")

@sample.route('/')
class SampleController(Resource):
    def get(self):
        """[summary]
        
        Raises:
            NotImplementedError: [description]
        """
        raise NotImplementedError

    def post(self):
        """[summary]
        
        Raises:
            NotImplementedError: [description]
        """
        raise NotImplementedError
    
    def delete(self):
        """[summary]
        """

        raise NotImplementedError
    




