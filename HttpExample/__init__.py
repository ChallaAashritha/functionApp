import json

import azure.functions as func

from config_loader import get_setting


def json_response(payload: dict, status_code: int = 200) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps(payload),
        status_code=status_code,
        mimetype="application/json"
    )


def main(req: func.HttpRequest) -> func.HttpResponse:
    greeting = get_setting("HTTP_GREETING")
    name = req.params.get('name')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            return json_response(
                {
                    "error": "Invalid JSON payload.",
                    "expectedPayload": {
                        "name": "Aashritha"
                    }
                },
                status_code=400
            )

        name = req_body.get('name') if isinstance(req_body, dict) else None

    if name:
        return json_response(
            {
                "message": f"{greeting}, {name}!",
                "name": name
            }
        )

    return json_response(
        {
            "error": "Missing required field: name.",
            "expectedPayload": {
                "name": "Aashritha"
            }
        },
        status_code=400
    )
