FROM python:3.13.13-alpine

ENV PATH="${PATH}:/root/.local/bin"
COPY . /app

ENV PYTHONPATH /app
WORKDIR /app
RUN pip install -r ./requirements.txt
RUN chmod +x ./start.sh
EXPOSE 8000
