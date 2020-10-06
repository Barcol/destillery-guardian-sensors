FROM python:3.7

COPY . ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
