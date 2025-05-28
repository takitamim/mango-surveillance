from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count
from .models import Grower, Plant, SurveillanceRecord
from .forms import GrowerForm, PlantForm, SurveillanceRecordForm

def home(request):
    severity_counts = SurveillanceRecord.objects.values('severity').annotate(count=Count('severity')).order_by('severity')
    counts = [0, 0, 0]  # Low, Medium, High
    for item in severity_counts:
        if item['severity'] == 'low':
            counts[0] = item['count']
        elif item['severity'] == 'medium':
            counts[1] = item['count']
        elif item['severity'] == 'high':
            counts[2] = item['count']
    return render(request, 'surveillance/home.html', {'severity_counts': counts})

class GrowerListView(ListView):
    model = Grower
    template_name = 'surveillance/grower_list.html'
    context_object_name = 'growers'

class GrowerDetailView(DetailView):
    model = Grower
    template_name = 'surveillance/grower_detail.html'

class GrowerCreateView(CreateView):
    model = Grower
    form_class = GrowerForm
    template_name = 'surveillance/grower_form.html'
    success_url = reverse_lazy('surveillance:grower_list')

class GrowerUpdateView(UpdateView):
    model = Grower
    form_class = GrowerForm
    template_name = 'surveillance/grower_form.html'
    success_url = reverse_lazy('surveillance:grower_list')

class GrowerDeleteView(DeleteView):
    model = Grower
    template_name = 'surveillance/grower_confirm_delete.html'
    success_url = reverse_lazy('surveillance:grower_list')

class PlantListView(ListView):
    model = Plant
    template_name = 'surveillance/plant_list.html'
    context_object_name = 'plants'

class PlantDetailView(DetailView):
    model = Plant
    template_name = 'surveillance/plant_detail.html'

class PlantCreateView(CreateView):
    model = Plant
    form_class = PlantForm
    template_name = 'surveillance/plant_form.html'
    success_url = reverse_lazy('surveillance:plant_list')

class PlantUpdateView(UpdateView):
    model = Plant
    form_class = PlantForm
    template_name = 'surveillance/plant_form.html'
    success_url = reverse_lazy('surveillance:plant_list')

class PlantDeleteView(DeleteView):
    model = Plant
    template_name = 'surveillance/plant_confirm_delete.html'
    success_url = reverse_lazy('surveillance:plant_list')

class RecordListView(ListView):
    model = SurveillanceRecord
    template_name = 'surveillance/record_list.html'
    context_object_name = 'records'

    def get_queryset(self):
        queryset = super().get_queryset()
        pest = self.request.GET.get('pest')
        if pest:
            queryset = queryset.filter(pest_or_disease__icontains=pest)
        return queryset

class RecordDetailView(DetailView):
    model = SurveillanceRecord
    template_name = 'surveillance/record_detail.html'
    context_object_name = 'record'

class RecordCreateView(CreateView):
    model = SurveillanceRecord
    form_class = SurveillanceRecordForm
    template_name = 'surveillance/record_form.html'
    success_url = reverse_lazy('surveillance:record_list')

class RecordUpdateView(UpdateView):
    model = SurveillanceRecord
    form_class = SurveillanceRecordForm
    template_name = 'surveillance/record_form.html'
    success_url = reverse_lazy('surveillance:record_list')

class RecordDeleteView(DeleteView):
    model = SurveillanceRecord
    template_name = 'surveillance/record_confirm_delete.html'
    success_url = reverse_lazy('surveillance:record_list')