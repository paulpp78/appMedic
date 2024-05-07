FROM golang
WORKDIR /app
COPY . /app
RUN "./serverGO/script"
EXPOSE 8080
CMD ["./serverGO/server"]