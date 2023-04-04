#!/usr/bin/env python3

import connexion
from connexion.resolver import MethodViewResolver
from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Api rest for globalhitss-api'}, pythonic_params=True,
                resolver=MethodViewResolver("swagger_server.controllers"))
    app.run(port=8080)


if __name__ == '__main__':
    main()
