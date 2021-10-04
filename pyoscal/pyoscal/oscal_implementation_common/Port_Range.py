class Port_Range:
    """Port Range

    Where applicable this is the IPv4 port range on which the service
operates.

    Attributes:
        start (nonNegativeInteger):Indicates the starting port
number in a port range

        end (nonNegativeInteger):Indicates the ending port number in
a port range

        transport (token):Indicates the transport type.

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-implementation-common",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
        "start",
        "end",
        "transport",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        use_name='port-range',
        start=None,
        end=None,
        transport=None,
        prose=None,
    ):
        self._start = None
        self.start = \
            start
        self._end = None
        self.end = \
            end
        self._transport = None
        self.transport = \
            transport
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            start=obj.get(
                'start',
                None),
            end=obj.get(
                'end',
                None),
            transport=obj.get(
                'transport',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def start(self):
        """Indicates the starting port number in a port range
        """
        return self._start

    @start.setter
    def start(self, x):
        self._start = x

    @property
    def end(self):
        """Indicates the ending port number in a port range
        """
        return self._end

    @end.setter
    def end(self, x):
        self._end = x

    @property
    def transport(self):
        """Indicates the transport type.
        """
        return self._transport

    @transport.setter
    def transport(self, x):
        self._transport = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
