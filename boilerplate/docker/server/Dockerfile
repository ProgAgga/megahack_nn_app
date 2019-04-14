FROM nikolaik/python-nodejs

ENV PYTHONUNBUFFERED 1
ENV DOCKERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN npm install
RUN npm run start
RUN chmod +x ./up.sh
