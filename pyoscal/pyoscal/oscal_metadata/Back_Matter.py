class Back_Matter:
    """Back matter

    A collection of resources, which may be included directly or by
reference.

    Attributes:
        prose (str):Default value holder for raw data in texts

        resource (ARRAY):A resource associated with content in the
containing document. A resource may be directly included in
the document base64 encoded or may point to one or more
equivalent internet resources.

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "resource",
    ]

    def __init__(
        self,
        use_name='back-matter',
        prose=None,
        resource=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._resource = None
        self.resource = \
            resource
        self.use_name = use_name
        if resource is None:
            self.resource = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            resource=obj.get(
                'resource',
                None),
        )
        newcls.resource = \
            obj.get('resources')
        return newcls

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def resource(self):
        """A resource associated with content in the containing document. A
        resource may be directly included in the document base64 encoded or
        may point to one or more equivalent internet resources.
        """
        return self._resource

    @resource.setter
    def resource(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._resource):
            self._resource = []
        if bool(x):
            if x != self._resource:
                self._resource += list(x)

    @property
    def resources(self):
        return self._resource

    @resources.setter
    def resources(self, x):
        self.resource(x)
