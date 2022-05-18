class Custom:
    """Custom grouping

    A Custom element frames a structure for embedding represented controls
in resolution.

    Attributes:
        prose (str):Default value holder for raw data in texts

        group (ARRAY):

        insert_controls (ARRAY):

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "group",
        "insert_controls",
    ]

    def __init__(
        self,
        use_name='custom',
        prose=None,
        group=None,
        insert_controls=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._group = None
        self.group = \
            group
        self._insert_controls = None
        self.insert_controls = \
            insert_controls
        self.use_name = use_name
        if group is None:
            self.group = []
        if insert_controls is None:
            self.insert_controls = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            group=obj.get(
                'group',
                None),
            insert_controls=obj.get(
                'insert_controls',
                None),
        )
        newcls.group = \
            obj.get('groups')
        newcls.insert_controls = \
            obj.get('insert_controls')
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
    def group(self):
        return self._group

    @group.setter
    def group(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._group):
            self._group = []
        if bool(x):
            if x != self._group:
                self._group += list(x)

    @property
    def groups(self):
        return self._group

    @groups.setter
    def groups(self, x):
        self.group(x)

    @property
    def insert_controls(self):
        return self._insert_controls

    @insert_controls.setter
    def insert_controls(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._insert_controls):
            self._insert_controls = []
        if bool(x):
            if x != self._insert_controls:
                self._insert_controls += list(x)
