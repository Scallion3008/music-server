FROM alpine:3.23.3

WORKDIR /telegram_bot

RUN apk add --update --no-cache ffmpeg

# Install uv and add to $PATH
RUN wget -O - https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Install Python packages before copying other files to better utilize build cache
COPY pyproject.toml pyproject.toml
RUN uv sync

COPY --exclude=music --exclude=pyproject.toml . .

CMD ["uv", "run", "main.py"]
