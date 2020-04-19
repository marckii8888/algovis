from django.urls import path
from  .views  import IndexView, plotInsertionSort, plotMergeSort, plotQuickSort, plotHeapSort

app_name='algo'

urlpatterns  =  [
    path('', IndexView.as_view() , name='index'),
    path('insertionsort/', plotInsertionSort, name='plotInsertionSort'),
    path('mergesort/', plotMergeSort, name='plotMergeSort'),
    path('quicksort/', plotQuickSort, name='plotQuickSort'),
    path('heapsort/',  plotHeapSort,  name='plotHeapSort'),
]
