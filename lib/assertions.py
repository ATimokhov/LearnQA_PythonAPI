from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        for name in names:
            assert name in response_as_dict, f"Response JSON shouldn't have key '{name}'. But it's present"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. But it's present"

    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        for name in names:
            assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}', but it is present."

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual {response.status_code}"

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_value_by_name(responce: Response, name, expected_value, error_message):
        try:
            responce_as_dict = responce.json()
        except json.JSONDecodeError:
            assert False, f"Responce is not in JSON format. Responce text is '{responce.text}'"

        assert name in responce_as_dict, f"Responce JSON doesn't have key '{name}'"
        assert responce_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_expected_response_content(response: Response, expected_content):
        assert response.content.decode('utf-8') == expected_content, \
            f"Unexpected response content: '{response.content}'"