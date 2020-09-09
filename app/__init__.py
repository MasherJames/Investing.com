import os

from flask import Flask, request, jsonify
from ariadne import (graphql_sync, load_schema_from_path,
                     QueryType, make_executable_schema)
from ariadne.constants import PLAYGROUND_HTML

from app.db.database import init_db, db_session
from app.graphql.resolvers import *
from app.graphql.directives import FormatDateDirective
from app.graphql.enums import company_name
from .config import app_config

# load schema
type_defs = load_schema_from_path("app/graphql/schema.graphql")

query = QueryType()

query.set_field("allCompanies", resolve_all_companies)
query.set_field("allHistoriacalData", resolve_all_historical_data)
query.set_field("companyHistoricalData", resolve_company_historical_data)

schema = make_executable_schema(type_defs, [query, company_name], directives={
                                "formatDate": FormatDateDirective})


def create_app():
    # Flask instance which is the WSGI application
    app = Flask(__name__)
    app.config.from_object(app_config[os.getenv("APP_SETTINGS")])
    app.config.from_pyfile('config.py')

    # Initialise the database and make it ready for use after the app starts
    with app.app_context():
        init_db()

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

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        ''' remove database sessions at the end of the request or when the application shuts down '''
        db_session.remove()

    return app
