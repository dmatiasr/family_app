# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Get the Real World example app
RUN git clone https://github.com/dmatiasr/family_app /deb/app

# how to change to the current branch?
# for now, apply manually.
RUN cd /deb/app && git checkout unit_test_stage_1
# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /deb/app

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

VOLUME /deb/app

EXPOSE 8080

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]
