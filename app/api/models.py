from flask_restplus import fields, Model

_sample_request = {"field": fields.String(required=True),
                     }

sample_request = Model("SampleRequest", _sample_request)

MODEL_LIST = [sample_request]