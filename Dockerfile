FROM python:3
WORKDIR /app
COPY ./requeriments.txt /app
RUN pip install -r ./requeriments.txt

COPY . .
EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]



