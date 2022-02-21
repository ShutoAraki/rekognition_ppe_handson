import json
import base64
from io import BytesIO
import boto3

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    # FYI: https://github.com/oecdx/python-lambda-rekognition-example/blob/master/lambda_function.py
    b64str = event["body"]
    req_image = base64.b64decode(b64str.encode("UTF-8"))

    image_bin = BytesIO(req_image)
    image = image_bin.getvalue()

    # docs: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_protective_equipment
    response = rekognition.detect_protective_equipment(
        Image = {
            "Bytes": image
        },
        SummarizationAttributes = {
            "MinConfidence": 80,
            "RequiredEquipmentTypes": [
                "FACE_COVER"
            ]
        }
    )
    print(response)
    return {
        'statusCode': 200,
        'body': response,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type,X-CSRF-TOKEN'
        }
    }
