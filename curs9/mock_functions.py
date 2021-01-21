import json
import requests


def yes_no_api_requests():
    request = requests.get('https://yesno.wtf/api')
    return {
        "data": json.loads(request.text),
        'code': request.status_code
    }


def is_yes_answer():
    request_data = yes_no_api_requests()
    print(request_data)
    answer = request_data["data"]["answer"]
    code = request_data['code']

    return answer == "yes" and code == 200


# print(yes_no_api_requests())
print(is_yes_answer())
