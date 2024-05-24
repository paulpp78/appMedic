FROM golang:1.22.2

WORKDIR /app

COPY ./serverGO /app

COPY . .

RUN go build -o server .

EXPOSE 8080

CMD ["./server"]
