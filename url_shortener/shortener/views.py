from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import URL
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def index(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        validator = URLValidator()
        try:
            validator(long_url)
            url, created = URL.objects.get_or_create(long_url=long_url)
            short_url = request.build_absolute_uri('/') + url.short_code
            return render(request, 'index.html', {'short_url': short_url})
        except ValidationError:
            messages.error(request, 'Invalid URL. Please enter a valid URL.')
    return render(request, 'index.html')


def redirect_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    url.click_count += 1
    url.save()
    return render(request, 'redirect.html', {'long_url': url.long_url})
