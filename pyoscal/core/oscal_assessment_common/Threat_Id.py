class Threat_Id:
    """Threat ID

    A pointer, by ID, to an externally-defined threat.

    Attributes:
        system (uri):Specifies the source of the threat information.

        href (uri-reference):An optional location for the threat
data, from which this ID originates.

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "system",
        "href",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        system,
        use_name='threat-id',
        href=None,
        prose=None,
    ):
        self._system = None
        self.system = \
            system
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
            system=obj.get(
                'system',
                None),
            href=obj.get(
                'href',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def system(self):
        """Specifies the source of the threat information.
        """
        return self._system

    @system.setter
    def system(self, x):
        self._system = x

    @property
    def href(self):
        """An optional location for the threat data, from which this ID
        originates.
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
