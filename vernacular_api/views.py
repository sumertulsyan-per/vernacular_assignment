from django.http import HttpResponse
from django.views.generic import View
import json
from vernacular_api.util import is_json
from vernacular_api.validators import validate_finite_values_entity, validate_numeric_values_entity


class FiniteEntity(View):
    def post(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            error_msg = {'msg': 'Please send valid json data only'}
            return HttpResponse(json.dumps(error_msg), content_type='application/json', status=400)

        py_data = json.loads(data)
        try:
            response = validate_finite_values_entity(py_data)
        except:
            response = {'msg': 'Json data not in correct format'}
            return HttpResponse(json.dumps(response), content_type='application/json', status=400)

        return HttpResponse(json.dumps(response), content_type='application/json', status=200)


class NumericEntity(View):
    def post(self, request, *args, **kwargs):
        data = request.body
        if not is_json(data):
            error_msg = {'msg': 'Please send valid json data only'}
            return HttpResponse(json.dumps(error_msg), content_type='application/json', status=400)

        py_data = json.loads(data)
        try:
            response = validate_numeric_values_entity(py_data)
        except:
            response = {'msg': 'Json data not in correct format'}
            return HttpResponse(json.dumps(response), content_type='application/json', status=400)

        return HttpResponse(json.dumps(response), content_type='application/json', status=200)


def index(request):
    msg = "Congrats!! vernacular_assignment App is working"
    return HttpResponse(msg)