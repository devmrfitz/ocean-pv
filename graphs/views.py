from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .functions import(
    return_ocean_descriptions_with_graph,
    clean_multiple_results_data,
    utility_function
)
from .forms import GraphSelector
from interactions.models import SelfAnswerGroup


@login_required
def single_result_view(request, pk):
    plot = return_ocean_descriptions_with_graph(pk)
    return render(request, 'graphs/individual_result.html', {'plot': plot})


@login_required
def multiple_result_view(request):
    answer_groups = SelfAnswerGroup.objects.filter(
        user_profile=request.user.profile)
    if request.method == 'POST':
        form = GraphSelector(request.POST)
        if form.is_valid():
            primary_keys = list(primary_key for primary_key in form.cleaned_data.get(
                'primary_key').split(',') if primary_key)

            valid_primary_keys, unavailable_answer_pks, duplicate_answer_pks = clean_multiple_results_data(
                *primary_keys)

            if unavailable_answer_pks:
                messages.info(request,
                              f"Some IDs you entered were invalid and have been filtered out")
            if duplicate_answer_pks:
                messages.info(request,
                              f"Some IDs you entered were duplicates and have been filtered out")

            plot, areas_list = utility_function(*valid_primary_keys)

            return render(request, 'graphs/multiple_results.html', {
                'form': form, 'answer_groups': answer_groups, 
                'plot': plot,
            })

    else:
        form = GraphSelector(request.GET or None)
    return render(request, 'graphs/multiple_results.html', {
        'form': form,
        'answer_groups': answer_groups
    })
