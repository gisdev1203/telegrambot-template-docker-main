FROM python:3.10.4-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry 

RUN poetry config virtualenvs.create false
RUN poetry install

CMD [ "python", "main.py" ]
