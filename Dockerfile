# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10

EXPOSE 5000:5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

ADD app.py /
WORKDIR /
COPY . /


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "app.py", "gunicorn", "--bind", "--host=0.0.0.0", "app:app"] 