from django.shortcuts import render
from .models import MovieData
from django.core.paginator import Paginator
# Create your views here.

def movie_list(request):
    movie_data = MovieData.objects.all()
    if request.method == 'POST':
        search_query = request.POST.get('search')
        if search_query:
            # Filter the movie_data queryset based on the search query
            movie_data = movie_data.filter(name__icontains=search_query)
    paginator = Paginator(movie_data, 3)
    page = request.GET.get("page")
    movie_data = paginator.get_page(page)
    context = {
        'page_obj': movie_data,
    }
    return render(request, "newapp/movie_list.html", context)

   