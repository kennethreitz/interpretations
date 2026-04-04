FROM nginx:alpine
COPY site/ /usr/share/nginx/html/
RUN cd /usr/share/nginx/html/mp3s && zip -0 ../interpretations-full-album.zip *.mp3
EXPOSE 80
