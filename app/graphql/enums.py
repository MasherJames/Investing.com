from ariadne import EnumType


company_name = EnumType(
    "CompanyName",
    {
        "Safaricom": "safaricom",
        "Absa": "absa",
    },
)
