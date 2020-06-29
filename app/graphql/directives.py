from ariadne import SchemaDirectiveVisitor
from graphql import default_field_resolver
from graphql.type import GraphQLString

from app.utils.date import format_date


class FormatDateDirective(SchemaDirectiveVisitor):
    def visit_field_definition(self, field, object_type):
        resolver = field.resolve or default_field_resolver
        date_format = self.args.get("format")

        def resolve_formatted_date(obj, info, **kwargs):
            date_string = resolver(obj, info, **kwargs)

            if date_string is None:
                return None
            if date_format:
                return format_date(date_string, date_format)
            return date_string
        field.resolve = resolve_formatted_date

        return field
