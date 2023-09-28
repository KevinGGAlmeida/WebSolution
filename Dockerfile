FROM  python

WORKDIR /app

RUN python -m pip flask

COPY . .

CMD ["python","App.py"]
