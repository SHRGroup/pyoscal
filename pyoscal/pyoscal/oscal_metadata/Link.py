class Link:
    """Link

    A reference to a local or remote resource

    Attributes:
        href (uri-reference):A resolvable URL reference to a
resource.

        rel (token):Describes the type of relationship provided by
the link. This can be an indicator of the link's purpose.

        media_type (str):

        prose (str):Default value holder for raw data in texts

        text (markup-line):A textual label to associate with the
link, which may be used for presentation in a tool.

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "href",
        "rel",
        "media_type",
    ]
    subcomponents = [
        "prose",
        "text",
    ]

    def __init__(
        self,
        href,
        use_name='link',
        rel=None,
        media_type=None,
        prose=None,
        text=None,
    ):
        self._href = None
        self.href = \
            href
        self._rel = None
        self.rel = \
            rel
        self._media_type = None
        self.media_type = \
            media_type
        self._prose = None
        self.prose = \
            prose
        self._text = None
        self.text = \
            text
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            href=obj.get(
                'href',
                None),
            rel=obj.get(
                'rel',
                None),
            media_type=obj.get(
                'media_type',
                None),
            prose=obj.get(
                'prose',
                None),
            text=obj.get(
                'text',
                None),
        )
        return newcls

    @property
    def href(self):
        """A resolvable URL reference to a resource.
        """
        return self._href

    @href.setter
    def href(self, x):
        self._href = x

    @property
    def rel(self):
        """Describes the type of relationship provided by the link. This can be
        an indicator of the link's purpose.
        """
        return self._rel

    @rel.setter
    def rel(self, x):
        self._rel = x

    @property
    def media_type(self):
        return self._media_type

    @media_type.setter
    def media_type(self, x):
        self._media_type = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def text(self):
        """A textual label to associate with the link, which may be used for
        presentation in a tool.
        """
        return self._text

    @text.setter
    def text(self, x):
        self._text = x
