FROM debian:stable-slim

WORKDIR /loadgen

COPY --from=ghcr.io/astral-sh/uv:0.9.0 /uv /uvx /bin/

COPY ./*.toml ./

RUN uv sync --compile-bytecode --no-cache

COPY ./entrypoint.sh ./

COPY ./*.py .

WORKDIR /loadgen

ENV PATH="/loadgen/.venv/bin:$PATH"

ENTRYPOINT ["./entrypoint.sh"]

