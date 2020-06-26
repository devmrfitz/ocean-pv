import json

from django.core.exceptions import ValidationError

def json_validator(json_string):
	json_data = json.loads(json_string)
	
	if json_data:
		pass
	else:
		raise ValidationError('The input seems to be corrupted')