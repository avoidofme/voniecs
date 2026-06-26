FROM golang:alpine AS builder

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN go build

FROM alpine:3

WORKDIR /app

COPY --from=builder /app/vonapi .

CMD [ "./vonapi" ]
