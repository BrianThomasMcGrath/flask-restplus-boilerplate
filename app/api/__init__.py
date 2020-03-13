from flask import Blueprint
from flask_restplus import Api

from app.api.controllers.controller import sample
from app.api.models import MODEL_LIST

blueprint = Blueprint('api', import_name=__name__)
api = Api(blueprint, name="SampleAPI", title="SampleAPI", description="Sample Flask Restplus API")

api.add_namespace(sample)

for model in MODEL_LIST:
    api.models[model.name] = model