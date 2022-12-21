from locust import HttpUser, task, between
from seldon_deploy_sdk import Configuration, PredictApi, ApiClient, SeldonDeploymentsApi, ModelMetadataServiceApi, DriftDetectorApi, BatchJobsApi, BatchJobDefinition
from seldon_deploy_sdk.auth import OIDCAuthenticator
from seldon_deploy_sdk.rest import ApiException


class HelloWorldUser(HttpUser):
    wait_time = between(1, 3)
    # SD_IP = "35.190.191.28"

    # config = Configuration()
    # config.host = f"http://{SD_IP}/seldon-deploy/api/v1alpha1"
    # config.oidc_server = f"http://{SD_IP}/auth/realms/deploy-realm"
    # config.oidc_client_id = "sd-api"
    # config.oidc_client_secret = "sd-api-secret"
    # config.username = "admin@seldon.io"
    # config.password = "12341234"
    # config.auth_method = "password_grant"

    # auth = OIDCAuthenticator(config)
    # config.id_token = auth.authenticate()

    # DEPLOYMENT_NAME = "wine-model-5"

    # SELDON_URL = f"/seldon/seldon/{DEPLOYMENT_NAME}/v2/models/{DEPLOYMENT_NAME}-container/infer"
    # headers = {
    #     "authorization": config.id_token
    # }

    @task
    def core_load_test(self):
        MODEL_NAME = "wines-classifier"
        NAMESPACE = "default"
        # /seldon/seldon/wine-model-5/v2/models/wine-model-5-container/infer

        SELDON_URL = f"/seldon/{NAMESPACE}/{MODEL_NAME}/api/v1.0/predictions"

        inference_request = {
            "data": {
                "names": ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"],
                "ndarray": [
                    [7, 0.27, 0.36, 20.7, 0.045, 45, 170, 1.001, 3, 0.45, 8.8]
                ]
            }
        }
        self.client.post(SELDON_URL, json=inference_request)
