from singer_sdk import typing as th
from tap_trello.schemas.utils.custom_schema_object import CustomObject


class BoardsObject(CustomObject):

    properties = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("desc", th.StringType),
        th.Property("descData", th.StringType),
        th.Property("closed", th.BooleanType),
        th.Property("dateClosed", th.DateTimeType),
        th.Property("idOrganization", th.StringType),
        th.Property("idEnterprise", th.StringType),
        th.Property("shortLink", th.StringType),
        th.Property("powerUps", th.ArrayType(th.StringType)),
        th.Property("dateLastActivity", th.DateTimeType),
        th.Property("dateLastView", th.DateTimeType),
        th.Property("shortUrl", th.StringType),
        th.Property("ixUpdate", th.StringType),
        th.Property("enterpriseOwned", th.BooleanType),
        th.Property("premiumFeatures", th.ArrayType(th.StringType)),
        th.Property("idMemberCreator", th.StringType)
    )
