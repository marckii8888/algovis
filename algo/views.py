from django.shortcuts import render
from  django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from .models import Algo

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'algo/index.html'
    context = {
        'title': 'Algo Vis',
        'about': 'This is a side project created using Django, matplotlib and BootStrap</br> It aims to learn how to apply Django web framework,  </br>  as well as understand how sorting algorithms works. </br> As of now, Insertion Sort, Merge Sort, Quick Sort and Heap Sort are implemented.'
    }
    def get(self, request):
        return render(request, self.template_name, self.context)
    


def plotInsertionSort(request):
    insertionsort = Algo.objects.filter(name = 'Insertion Sort')[0]
    context = {
        'title': insertionsort.name,
        'algo': insertionsort.video,
        'description': {
            'description' : insertionsort.description,
            'pseudo' : insertionsort.pseudocode,
            'code': insertionsort.code,
        }
    }
    return render(request, 'algo/index.html', context)


def plotMergeSort(request):
    mergesort = Algo.objects.filter(name = 'Merge Sort')[0]
    context = {
        'title': mergesort.name,
        'algo': mergesort.video,
        'description': {
            'description' : mergesort.description,
            'pseudo' : mergesort.pseudocode,
            'code': mergesort.code,
        }
    }
    return render(request, 'algo/index.html', context)


def plotQuickSort(request):
    quicksort = Algo.objects.filter(name = 'Quick Sort')[0]
    context = {
        'title': quicksort.name,
        'algo': quicksort.video, 
        'description': {
            'description' : quicksort.description,
            'pseudo' : quicksort.pseudocode,
            'code': quicksort.code,
        }
    }
    return  render(request, 'algo/index.html', context)

def plotHeapSort(request):
    heapsort = Algo.objects.filter(name = 'Heap Sort')[0]
    context = {
        'title': heapsort.name,
        'algo': heapsort.video,
        'description': {
            'description' : heapsort.description,
            'pseudo' : heapsort.pseudocode,
            'code': heapsort.code,
        }
    }
    return render(request, 'algo/index.html', context)
