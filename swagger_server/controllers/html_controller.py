from swagger_server.models.html import HTML  # noqa: E501


def root_get():  # noqa: E501
    """The main INDEX.html

     # noqa: E501


    :rtype: HTML
    """
    return open("swagger_client/index.html", encoding='utf-8').read()
