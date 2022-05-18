class Rlink:
    """Resource link

    A pointer to an external resource with an optional hash for
verification and change detection.

    Attributes:
        href (uri-reference):A resolvable URI reference to a
resource.

        media_type (str):

        prose (str):Default value holder for raw data in texts

        hash (ARRAY):

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "href",
        "media_type",
    ]
    subcomponents = [
        "prose",
        "hash",
    ]

    def __init__(
        self,
        href,
        use_name='rlink',
        media_type=None,
        prose=None,
        hash=None,
    ):
        self._href = None
        self.href = \
            href
        self._media_type = None
        self.media_type = \
            media_type
        self._prose = None
        self.prose = \
            prose
        self._hash = None
        self.hash = \
            hash
        self.use_name = use_name
        if hash is None:
            self.hash = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            href=obj.get(
                'href',
                None),
            media_type=obj.get(
                'media_type',
                None),
            prose=obj.get(
                'prose',
                None),
            hash=obj.get(
                'hash',
                None),
        )
        newcls.hash = \
            obj.get('hashes')
        return newcls

    @property
    def href(self):
        """A resolvable URI reference to a resource.
        """
        return self._href

    @href.setter
    def href(self, x):
        self._href = x

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
    def hash(self):
        return self._hash

    @hash.setter
    def hash(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._hash):
            self._hash = []
        if bool(x):
            if x != self._hash:
                self._hash += list(x)

    @property
    def hashes(self):
        return self._hash

    @hashes.setter
    def hashes(self, x):
        self.hash(x)
