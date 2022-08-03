FROM python:3.9 AS builder
COPY requirements.txt .

RUN pip install -r requirements.txt

FROM python:3.9-slim
WORKDIR /www/vringe

COPY --from=builder /root/.local /root/.local
COPY ./src .
ENV PATH=/root/,local:$PATH

CMD [ "python", "-u", "./vringe.py" ]