# syntax=docker/dockerfile:1

FROM golang:1.23-alpine AS builder

WORKDIR /build

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -o go-app main.go


FROM alpine:3.21

RUN apk add --no-cache ca-certificates tini

WORKDIR /app

COPY --from=builder /build/go-app .

RUN adduser -D -u 1000 appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

HEALTHCHECK --interval=15s --timeout=3s --start-period=10s --retries=3 \
    CMD wget -q -O- http://localhost:8080/healthz || exit 1

ENTRYPOINT ["/sbin/tini", "--"]

CMD ["./go-app", "-model-url", "http://python-model:8000"]