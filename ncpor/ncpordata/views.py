from django.shortcuts import render , redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import Institute, Project, Expedition, Member, Station
from .forms import MetadataForm
from .models import Metadata

from django.http import JsonResponse
from .models import State, ScienceTopic
from .models import Country,  ScienceCategory





# Home Page
def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html', context)

# About Page
def about(request):
    return render(request, 'about.html')

# Services Page
def services(request):
    return render(request, 'services.html')


from django.core.files.storage import FileSystemStorage
from .models import Metadata
from .forms import MetadataForm 

#datasubmission page
def datasubmission(request):
    years = ['2025', '2024', '2023', '2022', '2021', '2020']
    if request.method == "POST":
        form = MetadataForm(request.POST, request.FILES)


        if 'preview' in request.POST:
            if form.is_valid():
                return render(request, 'preview.html', {
                    'form': form,
                    'data': form.cleaned_data,
                    'years': years
                })
            else:
                print(" Errors found during preview:")
                for field, error in form.errors.items():
                    print(f"{field}: {error}")

        # submit logic
        elif form.is_valid():
            metadata = form.save()
            return redirect('success', pk=metadata.pk)
        else:
            print(" Errors found during submit:")
            for field, error in form.errors.items():
                print(f"{field}: {error}")
    else:
        form = MetadataForm()

    return render(request, 'datasubmission.html', {
        'form': form,
        'years': years,
    })

def get_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse(list(states), safe=False)

def get_topics(request):
    category_id = request.GET.get('category_id')
    topics = ScienceTopic.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(topics), safe=False)

def success(request, pk):
    metadata = Metadata.objects.get(pk=pk)

    if request.method == "POST":
        dataset_file = request.FILES.get('dataset_file')
        old_data = request.POST.get('old_data')

        if dataset_file or old_data:
            if dataset_file:
                metadata.dataset_file = dataset_file
            if old_data:
                metadata.old_data = old_data
            metadata.save()
            print(" Uploaded file and old data saved!")
            return redirect('success', pk=metadata.pk)  # Reload success page with updated data

    return render(request, 'success.html', {'metadata': metadata})





    

# Polar Directory Page (Search Logic Here)
def polardirectory(request):
    results = []

    if request.method == 'POST':
        selected_type = request.POST.get('type')
        selected_station = request.POST.get('station')

        # Search by entity type
        if selected_type == 'institute':
            results = Institute.objects.all()
        elif selected_type == 'project':
            results = Project.objects.all()
        elif selected_type == 'member':
            results = Member.objects.all()
        elif selected_type == 'expedition':
            results = Expedition.objects.all()
        elif selected_type == 'role':
            results = Member.objects.values('role').distinct()
        elif selected_type == 'leader':
            results = Member.objects.filter(role__icontains='leader')
        elif selected_type == 'keyword':
            results = Project.objects.filter(title__icontains='antarctica')  # You can make this dynamic later

        # Search by station
        if selected_station:
            results = Station.objects.filter(name=selected_station)

    return render(request, 'polardirectory.html', {'results': results})


