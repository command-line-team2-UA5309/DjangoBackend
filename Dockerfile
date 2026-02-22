FROM python:3.13-slim
 
RUN mkdir /app
WORKDIR /app
 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 
 
RUN pip install --upgrade pip 
COPY requirements.txt  /app/
RUN pip install --no-cache-dir -r requirements.txt
 
COPY . /app/
 
EXPOSE 8000
 
CMD ["gunicorn", "configs.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]