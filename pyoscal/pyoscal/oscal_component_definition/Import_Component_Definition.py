class Import_Component_Definition:
    """Import Component Definition

    Loads a component definition from another resource.

    Attributes:
        href (uri-reference):A link to a resource that defines a set
of components and/or capabilities to import into this
collection.

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-component-definition",
        "oscal-implementation-common",
    ]
    parameters = [
        "href",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        href,
        use_name='import-component-definition',
        prose=None,
    ):
        self._href = None
        self.href = \
            href
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            href=obj.get(
                'href',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def href(self):
        """A link to a resource that defines a set of components and/or
        capabilities to import into this collection.
        """
        return self._href

    @href.setter
    def href(self, x):
        self._href = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
