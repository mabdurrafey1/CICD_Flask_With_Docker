FROM python:3.9-alpine

WORKDIR /usr/src/app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Let' only copy the required files and folders

COPY ./ ./

EXPOSE 5000

# CMD ["python", "application.py" ]
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
