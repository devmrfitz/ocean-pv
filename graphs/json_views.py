from django.http import JsonResponse

from interactions.models import SelfAnswerGroup


def update_accuracy(request):
    if request.method == 'GET' or request.is_ajax():
        accuracy = request.GET.get('accuracy')
        pk = request.GET.get('pk')
        answer_group = SelfAnswerGroup.objects.get(pk=pk)
        if answer_group.accuracy:
        	return JsonResponse(
        	{'error':True, 
        	'message': 'You have already provided feedback for this test'}
        	)
        answer_group.accuracy = accuracy
        answer_group.save()
        return JsonResponse(
        {'error': False, 
        'message': 'Your feedback has been saved successfully!'}
        )
