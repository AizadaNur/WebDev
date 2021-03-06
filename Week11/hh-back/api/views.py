from django.http import JsonResponse
from api.models import Company, Vacancy


def companies_list(request):
    companies = Company.objects.all()
    json_companies = [c.to_json() for c in companies]
    return JsonResponse(json_companies, safe=False)


def company_detail(request, pk):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    return JsonResponse(company.to_json())


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    json_vacancies = [v.to_json() for v in vacancies]
    return JsonResponse(json_vacancies, safe=False)


def vacancy_detail(request, pk):
    try:
        vacancy = Vacancy.objects.get(id=pk)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    return JsonResponse(vacancy.to_json())


def company_vacancies(request, pk):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    vacancies = company.vacancy_set.all()
    json_vacancies = [v.to_json() for v in vacancies]
    return JsonResponse(json_vacancies, safe=False)


def top_ten(request):
    top10 = Vacancy.objects.order_by('-salary')[:10]
    json_top10 = [v1.to_json() for v1 in top10]
    return JsonResponse(json_top10, safe=False)
