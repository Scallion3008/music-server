FROM ngrok/ngrok:3.23.3-alpine

USER root
RUN apk add --update --no-cache jq curl

# This is dumb as fuck.
# Default user 'ngrok' has its shell set to the ngrok executable, so...
USER ngrok
CMD ["tcp", "2222"]
