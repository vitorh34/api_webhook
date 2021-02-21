# pull official base image
FROM python:3.6

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# add app
COPY . .

CMD uvicorn main:app --host 0.0.0.0
