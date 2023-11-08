FROM python:3.7
COPY . ../codingChallenge
WORKDIR /codingChallenge
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["main.py"]