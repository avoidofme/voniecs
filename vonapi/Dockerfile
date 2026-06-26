FROM golang:alpine

WORKDIR /app

COPY . .

RUN go get

CMD [ "go", "run", "." ]
