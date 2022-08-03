FROM python:3.9
WORKDIR /www/vringe
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD vringe.py ./
CMD [ "python", "./vringe.py" ]