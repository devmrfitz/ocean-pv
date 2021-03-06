from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .functions import(
    return_ocean_descriptions_with_graph,
    ultimate_wrapper,
)
from .forms import GraphSelector
from interactions.models import SelfAnswerGroup


@login_required
def single_result_view(request, pk):
    plot = return_ocean_descriptions_with_graph(pk)
    return render(request, 'graphs/individual_result.html', {'plot': plot})


@login_required
def multiple_result_view(request):
    if request.method == 'POST':
        form = GraphSelector(request.user, request.POST)
        if form.is_valid():
            primary_keys = list(primary_key for primary_key in form.cleaned_data.get(
                'primary_key').split(',') if primary_key)
            try:
                valid_primary_keys, unavailable_answer_pks, duplicate_answer_pks, percentage_list, plot = ultimate_wrapper(
                    *primary_keys)
            except:
                return HttpResponse('You entered corrupted data')

            if unavailable_answer_pks:
                messages.info(request,
                              "Some IDs you entered were invalid and have been filtered out")
            if duplicate_answer_pks:
                messages.info(request,
                              "Some IDs you entered were duplicates and have been filtered out")

            return render(request, 'graphs/multiple_results.html', {
                'form': form,
                'plot': plot, 'percentage_list': percentage_list
            })

    else:
        form = GraphSelector(request.user)
    return render(request, 'graphs/multiple_results.html', {
        'form': form,
    })
