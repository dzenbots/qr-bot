FROM jjanzic/docker-python3-opencv

ENV TZ=Europe/Moscow

RUN git clone https://github.com/dzenbots/qr-bot.git
RUN cd qr-bot
WORKDIR qr-bot
RUN pip install numpy
RUN pip install -r requirements.txt
RUN mkdir temp

CMD python app.py
