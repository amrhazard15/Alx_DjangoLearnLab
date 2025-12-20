from django.http import HttpResponse
from django.urls import reverse

def home(request):
    html = f"""
    <h1>Welcome to Social Media API!</h1>
    <ul>
        <li><a href="{reverse('admin:index')}">Admin Panel</a></li>
        <li><a href="/accounts/">Accounts App</a></li>
        <li><a href="/api/">Posts & Notifications API</a></li>
        <li><a href="/swagger/">Swagger Documentation</a></li>
        <li><a href="/redoc/">Redoc Documentation</a></li>
    </ul>
    """
    return HttpResponse(html)

