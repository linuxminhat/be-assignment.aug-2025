FROM ghcr.io/astral-sh/uv:python3.11-bookworm
WORKDIR /riverflow-api
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project
ADD pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen
ENV PATH="/riverflow-api/.venv/bin:$PATH"
# ENV PYTHONPATH="/riverflow-api/app"
ENTRYPOINT []
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
