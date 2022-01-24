FROM python
WORKDIR /tests_project/
COPY Requirements.txt .
RUN pip install -r Requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=test_results/ /tests_project/tests/