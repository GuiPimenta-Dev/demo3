from infra.services import Services

class ErrorConfig:
    def __init__(self, services: Services) -> None:

        function = services.aws_lambda.create_function(
            name="Error",
            path="./functions/error",
            description="A mock of an error",
            
        )

        services.api_gateway.create_endpoint("GET", "/error", function, public=True)

            