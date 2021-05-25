class Attestation:
    """Attestation Statements

    A set of textual statements, typically written by the assessor.

    Attributes:
        prose (str):Default value holder for raw data in texts

        responsible_party (BY_KEY):

        part (ARRAY):

    """

    contexts = [
        "oscal-ar",
        "oscal-metadata",
        "oscal-assessment-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "responsible_party",
        "part",
    ]

    def __init__(
        self,
        part,
        use_name='attestation',
        prose=None,
        responsible_party=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._responsible_party = None
        self.responsible_party = \
            responsible_party
        self._part = None
        self.part = \
            part
        self.use_name = use_name
        if responsible_party is None:
            self.responsible_party = []
        if part is None:
            self.part = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            responsible_party=obj.get(
                'responsible_party',
                None),
            part=obj.get(
                'part',
                None),
        )
        newcls.responsible_party = \
            obj.get('responsible_parties')
        newcls.part = \
            obj.get('parts')
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
    def responsible_party(self):
        return self._responsible_party

    @responsible_party.setter
    def responsible_party(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._responsible_party):
            self._responsible_party = []
        if bool(x):
            if x != self._responsible_party:
                self._responsible_party += list(x)

    @property
    def responsible_parties(self):
        return self._responsible_party

    @responsible_parties.setter
    def responsible_parties(self, x):
        self.responsible_party(x)

    @property
    def part(self):
        return self._part

    @part.setter
    def part(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._part):
            self._part = []
        if bool(x):
            if x != self._part:
                self._part += list(x)

    @property
    def parts(self):
        return self._part

    @parts.setter
    def parts(self, x):
        self.part(x)
