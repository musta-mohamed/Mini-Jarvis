from django.http import HttpResponse
from django.conf import settings
from django.urls import path
from django.core.management import execute_from_command_line
import sys

# Basic settings
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
)

# View function
def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Port What</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; }
            h1 { color: #333; }
            p { font-size: 20px; }
        </style>
    </head>
    <body>
        <h1>Welcome to Port What</h1>
        <p>This is a simple Django website in one file!</p>
    </body>
    </html>
    """)

# URL patterns
urlpatterns = [
    path("", home),
]

# Run the server
if __name__ == "__main__":
    execute_from_command_line(sys.argv)
