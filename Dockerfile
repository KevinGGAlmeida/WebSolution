FROM  python

WORKDIR /app

RUN python -m pip install flask flask_session

COPY . .

CMD ["python","App.py"]
