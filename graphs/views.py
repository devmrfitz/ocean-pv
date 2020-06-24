from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .functions import (
    return_ocean_descriptions_with_graph,
    return_plot_and_view_data,
)
from .forms import GraphSelector


from pprint import pprint as print 



@login_required
def single_result_view(request, pk):
    plot = return_ocean_descriptions_with_graph(pk)
    return render(request, 'graphs/individual_result.html', {'plot': plot})


@login_required
def multiple_result_view(request):
    if request.method == 'POST':
        form = GraphSelector(request.user, request.POST)
        if form.is_valid():
            primary_keys = list(
                primary_key for
                primary_key in form.cleaned_data.get('primary_key').split(',')
                if primary_key
            )
            
            view_dict = {
            'master': form.cleaned_data.get('answer_group'),
            'to_plot': primary_keys
            }
            
            valid_dict, unavailable_pks, duplicate_pks, plot = return_plot_and_view_data(
                    view_dict) 
            
            # return HttpResponse('You entered corrupted data')
            
            print(valid_dict)
            if unavailable_pks:
                messages.info(
                    request,
                    "Invalid entries and have been filtered out"
                )
            if duplicate_pks:
                messages.info(
                    request,
                    "Duplicate entries have been filtered out"
                )

            return render(request, 'graphs/multiple_results.html', {
                'form': form,
                'plot': plot, 'percentage_list': 'percentage_list'
            })

    else:
        form = GraphSelector(request.user)
    return render(request, 'graphs/multiple_results.html', {
        'form': form,
    })
