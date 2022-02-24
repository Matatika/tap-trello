from singer_sdk import typing as th
from tap_trello.schemas.utils.custom_schema_object import CustomObject


class CardsObject(CustomObject):

    properties = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("badges", th.ObjectType(
            th.Property("attachmentByType", th.ObjectType(
                th.Property("trello", th.ObjectType(
                    th.Property("board", th.NumberType), 
                    th.Property("card", th.NumberType),
                ))
            )),
            th.Property("location", th.BooleanType),
            th.Property("votes", th.NumberType),
            th.Property("viewingMemberVoted", th.BooleanType),
            th.Property("subscribed", th.BooleanType),
            th.Property("fogbugz", th.StringType),
            th.Property("checkItems", th.NumberType),
            th.Property("checkItemsChecked", th.NumberType),
            th.Property("checkItemsEarliestDue", th.StringType),
            th.Property("comments", th.NumberType),
            th.Property("attachments", th.NumberType),
            th.Property("description", th.BooleanType),
            th.Property("due", th.StringType),
            th.Property("dueComplete", th.BooleanType),
            th.Property("start", th.BooleanType),
        )),
        th.Property("checkItemStates", th.StringType),
        th.Property("closed", th.BooleanType),
        th.Property("dueComplete", th.BooleanType),
        th.Property("dateLastActivity", th.StringType),
        th.Property("desc", th.StringType),
        th.Property("due", th.StringType),
        th.Property("dueReminder", th.StringType),
        th.Property("email", th.StringType),
        th.Property("idBoard", th.StringType),
        th.Property("idChecklists", th.ArrayType(th.StringType)),
        th.Property("idList", th.StringType),
        th.Property("idMembers", th.ArrayType(th.ObjectType())),
        th.Property("idMembersVoted", th.ArrayType(th.ObjectType())),
        th.Property("idShort", th.NumberType),
        th.Property("idAttachmentCover", th.StringType),
        th.Property("labels", th.ArrayType(th.ObjectType())),
        th.Property("idLabels", th.ArrayType(th.ObjectType())),
        th.Property("manualCoverAttachment", th.BooleanType),
        th.Property("name", th.StringType),
        th.Property("pos", th.NumberType),
        th.Property("shortLink", th.StringType),
        th.Property("shortUrl", th.StringType),
        th.Property("start", th.StringType),
        th.Property("subscribed", th.BooleanType),
        th.Property("url", th.StringType),
        th.Property("isTemplate", th.BooleanType),
        th.Property("cardRole", th.StringType),
    )
