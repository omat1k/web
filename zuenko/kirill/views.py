from django.http import HttpResponse

# Представление для страницы /info
def info_view(request):
    full_name = "Зуенко Кирилл Иванович"
    return HttpResponse(f"ФИО: {full_name}")

# Представление для страницы /group
def group_view(request):
    group = "БИН-22-01"
    return HttpResponse(f"Группа: {group}")

# Представление для страницы /age
def age_view(request):
    age = 19  
    return HttpResponse(f"Возраст: {age}")

def home_view(request):
    return HttpResponse("Это главная страница")