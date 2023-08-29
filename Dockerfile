FROM python:3.11

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080

COPY . .
ENTRYPOINT [ "streamlit", "run" ]
CMD ["index.py", "--server.port", "8080"]