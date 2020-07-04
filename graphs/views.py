from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormMixin
from django.views.generic import TemplateView

from mixins import CustomLoginRequiredMixin
from .functions import (
    return_ocean_descriptions_with_graph,
    return_plot_and_view_data,
)
from .forms import GraphSelector, AccuracySetterForm


class IndividualResultView(CustomLoginRequiredMixin, FormMixin, TemplateView):
	form_class = AccuracySetterForm
	template_name = 'graphs/individual_result.html'
	
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		plot, descriptions = return_ocean_descriptions_with_graph(self.kwargs.get('pk'))
		context['plot'] = plot
		context['descriptions'] = descriptions
		
		return context
	
	def get_initial(self, *args, **kwargs):
		initial = super().get_initial(*args, **kwargs)
		initial['pk'] = self.kwargs.get('pk')
		return initial
		

@login_required
def single_result_view(request, pk):
    form = AccuracySetterForm()
    plot, descriptions = return_ocean_descriptions_with_graph(pk)
    return render(request, 'graphs/individual_result.html',
                  {'plot': plot, 'form': form,
                   'descriptions': descriptions})

@ login_required
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

            valid_dict, unavailable_pks, duplicate_pks, plot = (
                return_plot_and_view_data(
                    view_dict
                )
            )
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
                'plot': plot, 'description_data': valid_dict
            })

    else:
        form = GraphSelector(request.user)
    return render(request, 'graphs/multiple_results.html', {
        'form': form,
    })
