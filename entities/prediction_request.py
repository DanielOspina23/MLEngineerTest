from validx import Dict, Int, Str, Float


class predictionRequest:

    template_prediction = Dict(
        schema={
            'order_id': Int(coerce=True),
            'store_id': Int(coerce=True),
            'to_user_distance': Float(),
            'to_user_elevation': Float(),
            'total_earning': Int(coerce=True),
            'created_at': Str()
        }
    )

    @classmethod
    def validate_request(cls, request: dict):
        return cls.template_prediction(request)
