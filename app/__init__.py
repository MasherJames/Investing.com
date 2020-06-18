import os

from flask import Flask, request, jsonify
from ariadne import (graphql_sync, load_schema_from_path,
                     QueryType, make_executable_schema)
from ariadne.constants import PLAYGROUND_HTML

from app.graphql.resolvers import resolve_hello
from .config import app_config

# load schema
type_defs = load_schema_from_path("app/graphql/schema.graphql")

query = QueryType()

query.set_field("hello", resolve_hello)

schema = make_executable_schema(type_defs, query)


def create_app():
    # Flask instance which is the WSGI application
    app = Flask(__name__)
    app.config.from_object(app_config[os.getenv("APP_SETTINGS")])
    app.config.from_pyfile('config.py')

    @app.route("/graphql", methods=["GET"])
    def graphql_playground():
        ''' On GET request serve GraphQL Playground '''
        return PLAYGROUND_HTML, 200

    @app.route("/graphql", methods=["POST"])
    def graphql_server():
        ''' All graphql requests are always sent as post request '''
        data = request.get_json()

        success, result = graphql_sync(
            schema, data, context_value=request, debug=app.debug)

        status_code = 200 if success else 400
        return jsonify(result), status_code

    return app
