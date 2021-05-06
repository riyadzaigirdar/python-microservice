FROM python

MAINTAINER Riyad Zaigirdar

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip 

RUN pip install -r requirements.txt

EXPOSE 8000

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
# RUN adduser -D user
# RUN chown -R user:user /vol/
RUN chown -R 755 /vol/
RUN chmod -R 755 /vol/web
# USER user

# RUN python manage.py migrate

# RUN python manage.py runserver 0.0.0.0:8000