class Protocol:
    """Service Protocol Information

    Information about the protocol used to provide a service.

    Attributes:
        uuid (uuid):A globally unique identifier that can be used to
reference this service protocol entry elsewhere in an OSCAL
document. A UUID should be consistently used for a given
resource across revisions of the document.

        name (str):The common name of the protocol, which should be
the appropriate "service name" from the

        prose (str):Default value holder for raw data in texts

        title (markup-line):A human readable name for the protocol
(e.g., Transport Layer Security).

        port_range (ARRAY):

    """

    contexts = [
        "oscal-implementation-common",
        "oscal-metadata",
    ]
    parameters = [
        "uuid",
        "name",
    ]
    subcomponents = [
        "prose",
        "title",
        "port_range",
    ]

    def __init__(
        self,
        name,
        use_name='protocol',
        uuid=None,
        prose=None,
        title=None,
        port_range=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._name = None
        self.name = \
            name
        self._prose = None
        self.prose = \
            prose
        self._title = None
        self.title = \
            title
        self._port_range = None
        self.port_range = \
            port_range
        self.use_name = use_name
        if port_range is None:
            self.port_range = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid=obj.get(
                'uuid',
                None),
            name=obj.get(
                'name',
                None),
            prose=obj.get(
                'prose',
                None),
            title=obj.get(
                'title',
                None),
            port_range=obj.get(
                'port_range',
                None),
        )
        newcls.port_range = \
            obj.get('port_ranges')
        return newcls

    @property
    def uuid(self):
        """A globally unique identifier that can be used to reference this
        service protocol entry elsewhere in an OSCAL document. A UUID should
        be consistently used for a given resource across revisions of the
        document.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def name(self):
        """The common name of the protocol, which should be the appropriate
        "service name" from the
        """
        return self._name

    @name.setter
    def name(self, x):
        self._name = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def title(self):
        """A human readable name for the protocol (e.g., Transport Layer
        Security).
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def port_range(self):
        return self._port_range

    @port_range.setter
    def port_range(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._port_range):
            self._port_range = []
        if bool(x):
            if x != self._port_range:
                self._port_range += list(x)

    @property
    def port_ranges(self):
        return self._port_range

    @port_ranges.setter
    def port_ranges(self, x):
        self.port_range(x)
