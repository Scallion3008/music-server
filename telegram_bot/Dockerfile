FROM python:3.14.3-alpine3.23

RUN apk add --update --no-cache ffmpeg

# Install pip requirements before copying other files to better utilize build cache
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && pip cache purge

COPY . .

CMD ["python3", "main.py"]
