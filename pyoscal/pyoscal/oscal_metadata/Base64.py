class Base64:
    """Base64

    The Base64 alphabet in RFC 2045 - aligned with XSD.

    Attributes:
        filename (uri-reference):Name of the file before it was
encoded as Base64 to be embedded in a

        media_type (str):

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "filename",
        "media_type",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        use_name='base64',
        filename=None,
        media_type=None,
        prose=None,
    ):
        self._filename = None
        self.filename = \
            filename
        self._media_type = None
        self.media_type = \
            media_type
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            filename=obj.get(
                'filename',
                None),
            media_type=obj.get(
                'media_type',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def filename(self):
        """Name of the file before it was encoded as Base64 to be embedded in a
        """
        return self._filename

    @filename.setter
    def filename(self, x):
        self._filename = x

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
