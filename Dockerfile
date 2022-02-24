FROM python:3.9

RUN git clone https://github.com/dzenbots/qr-bot.git

WORKDIR ./qr-bot
ENV TZ=Europe/Moscow

RUN pip install --no-cache-dir -r requirements.txt
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

CMD /wait && python app.py
