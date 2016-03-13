FROM python:3.4
ENV PYTHONBUFFERED 1
ENV DJANGO_CONFIGURATION Docker
ENV DJANGO_SETTINGS_MODULE asvs.settings.base
ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements/base.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input
CMD ["gunicorn", "-c", "gunicorn_conf.py", "asvs.wsgi:application", "--reload"]

