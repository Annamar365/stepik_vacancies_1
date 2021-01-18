from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render

from vacancies.models import Vacancy, Company, Specialty


def main_view(request):

    dict_temp = dict()
    specialty_dict = dict()
    company_dict = dict()
    context = dict()

    for specialty in Specialty.objects.all():
        dict_temp['code'] = specialty.code
        dict_temp['title'] = specialty.title
        dict_temp['cnt_by_specialty'] = Vacancy.objects.filter(specialty_id=specialty.id).count()

        specialty_dict[specialty.id] = dict_temp.copy()
        dict_temp.clear()

    context['specialty_list'] = specialty_dict

    for company in Company.objects.all():
        dict_temp['name'] = company.name
        dict_temp['cnt_by_company'] = Vacancy.objects.filter(company_id=company.id).count()

        if dict_temp['cnt_by_company'] == 1:
            dict_temp['cnt_label'] = "вакансия"
        else:
            dict_temp['cnt_label'] = "вакансий"

        company_dict[company.id] = dict_temp.copy()
        dict_temp.clear()

    context['company_list'] = company_dict

    return render(request, "index.html", context=context)


def create_vacancies_dict(vacancies_filter):

    vacancies_temp = dict()
    vacancies_dict = dict()

    for vacancy in vacancies_filter:
        vacancies_temp['id'] = vacancy.id
        vacancies_temp['title'] = vacancy.title
        vacancies_temp['skills'] = str(vacancy.skills).replace(",", " •")
        vacancies_temp['salary_min'] = vacancy.salary_min
        vacancies_temp['salary_max'] = vacancy.salary_max
        vacancies_temp['specialty'] = Specialty.objects.get(id=vacancy.specialty_id).title
        vacancies_temp['published_at'] = vacancy.published_at
        vacancies_temp['company_id'] = vacancy.company_id
        vacancies_temp['description'] = vacancy.description

        vacancies_dict[vacancy.id] = vacancies_temp.copy()
        vacancies_temp.clear()

    return vacancies_dict


def vacancies_view(request):

    context = dict()

    vacancies_dict = create_vacancies_dict(Vacancy.objects.all())

    context['vacancies_dict'] = vacancies_dict
    context['vacancies_count'] = len(vacancies_dict)
    context['main_title'] = "Все вакансии"

    return render(request, "vacancies.html", context=context)


def vacancies_cat_view(request, cat):

    context = dict()

    vacancies_dict = create_vacancies_dict(Vacancy.objects.filter(specialty__code=cat))

    context['vacancies_dict'] = vacancies_dict
    context['vacancies_count'] = len(vacancies_dict)
    context['main_title'] = Specialty.objects.get(code=cat).title

    return render(request, "vacancies.html", context=context)


def company_view(request, company_id):

    context = dict()

    vacancies_dict = create_vacancies_dict(Vacancy.objects.filter(company__id=company_id))

    context['vacancies_dict'] = vacancies_dict
    context['vacancies_count'] = len(vacancies_dict)
    context['company_name'] = Company.objects.get(id=company_id).name
    context['company_location'] = Company.objects.get(id=company_id).location

    if context['vacancies_count'] == 1:
        context['cnt_label'] = "вакансия"
    else:
        context['cnt_label'] = "вакансий"

    return render(request, "company.html", context=context)


def vacancy_view(request, vacancy_id):

    context = dict()

    vacancies_dict = create_vacancies_dict(Vacancy.objects.filter(id=vacancy_id))

    for vacancy_list in vacancies_dict.values():
        context['vacancies_dict'] = vacancy_list

    company_id = context['vacancies_dict']['company_id']

    context['company_name'] = Company.objects.get(id=company_id).name
    context['company_location'] = Company.objects.get(id=company_id).location
    context['company_employee'] = Company.objects.get(id=company_id).employee_count
    context['company_description'] = Company.objects.get(id=company_id).description

    return render(request, "vacancy.html", context=context)


def custom_handler404(request, *args):
    return HttpResponse("Что-то пошло не так!")


def custom_handler500(request, *args):
    return HttpResponseNotFound("Что-то пошло не так!")
