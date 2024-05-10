FROM python:3.11
WORKDIR /turing_test
COPY . .
RUN pip3 install -r requirements.txt
CMD [ "uvicorn","run","app:app","--host","0.0.0.0","--port","80","--workers","2" ]