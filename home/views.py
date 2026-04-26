from django.http import HttpResponse, HttpRequest


def home_view(request: HttpRequest) -> HttpResponse:
    """Return welcome message for the home page"""
    return HttpResponse("Ласкаво просимо на головну сторінку")


def about_view(request: HttpRequest) -> HttpResponse:
    """Return text for the about page"""
    return HttpResponse("Сторінка про нас")


def contact_view(request: HttpRequest) -> HttpResponse:
    """Return text for the contact page"""
    return HttpResponse("Зв'яжіться з нами")


def post_view(request: HttpRequest, id: int) -> HttpResponse:
    """Return message with post ID"""
    return HttpResponse(f"Ви переглядаєте пост з ID: {id}")


def profile_view(request: HttpRequest, username: str) -> HttpResponse:
    """Return message with the username"""
    return HttpResponse(f"Ви переглядаєте профіль користувача: {username}")


def event_view(request: HttpRequest, year: str, month: str, day: str) -> HttpResponse:
    """Return formatted event date"""
    return HttpResponse(f"Дата події: {year}-{month}-{day}")