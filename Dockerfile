FROM  python

WORKDIR /app

RUN python -m pip install flask

COPY . .

CMD ["python","App.py"]
