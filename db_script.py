# -*- coding: utf-8 -*-

import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'stepik_vacancies.settings'
django.setup()

from vacancies.models import Vacancy, Company, Specialty

import data


if __name__ == '__main__':

    for specialty_data in data.specialties:
        Specialty.objects.create(
            code=specialty_data['code'],
            title=specialty_data['title'],
        )

    for company_data in data.companies:
        Company.objects.create(
            id=int(company_data['id']),
            name=company_data['title'],
            location=company_data['location'],
            description=company_data['description'],
            employee_count=int(company_data['employee_count']),
        )

    for vacancy_data in data.jobs:
        Vacancy.objects.create(
            title=vacancy_data['title'],
            specialty=Specialty.objects.get(code=vacancy_data['specialty']),
            company=Company.objects.get(id=vacancy_data['company']),
            skills=vacancy_data['skills'],
            description=vacancy_data['description'],
            salary_min=int(vacancy_data['salary_from']),
            salary_max=int(vacancy_data['salary_to']),
            published_at=vacancy_data['posted'],
        )
