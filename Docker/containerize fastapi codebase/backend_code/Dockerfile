FROM python:3.12
RUN pip install poetry
WORKDIR /copy
COPY ./pyproject.toml /copy/
ADD ./backend_code /copy/backend_code/
RUN poetry install
CMD ["poetry", "run", "uvicorn", "backend_code.main:app", "--host", "localhost"]