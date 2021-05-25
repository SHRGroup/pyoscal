class Alter:
    """Alteration

    An Alter element specifies changes to be made to an included control
when a profile is resolved.

    Attributes:
        control_id (str):

        prose (str):Default value holder for raw data in texts

        remove (ARRAY):

        add (ARRAY):

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
        "control_id",
    ]
    subcomponents = [
        "prose",
        "remove",
        "add",
    ]

    def __init__(
        self,
        use_name='alter',
        control_id=None,
        prose=None,
        remove=None,
        add=None,
    ):
        self._control_id = None
        self.control_id = \
            control_id
        self._prose = None
        self.prose = \
            prose
        self._remove = None
        self.remove = \
            remove
        self._add = None
        self.add = \
            add
        self.use_name = use_name
        if remove is None:
            self.remove = []
        if add is None:
            self.add = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            control_id=obj.get(
                'control_id',
                None),
            prose=obj.get(
                'prose',
                None),
            remove=obj.get(
                'remove',
                None),
            add=obj.get(
                'add',
                None),
        )
        newcls.remove = \
            obj.get('removes')
        newcls.add = \
            obj.get('adds')
        return newcls

    @property
    def control_id(self):
        return self._control_id

    @control_id.setter
    def control_id(self, x):
        self._control_id = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def remove(self):
        return self._remove

    @remove.setter
    def remove(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._remove):
            self._remove = []
        if bool(x):
            if x != self._remove:
                self._remove += list(x)

    @property
    def removes(self):
        return self._remove

    @removes.setter
    def removes(self, x):
        self.remove(x)

    @property
    def add(self):
        return self._add

    @add.setter
    def add(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._add):
            self._add = []
        if bool(x):
            if x != self._add:
                self._add += list(x)

    @property
    def adds(self):
        return self._add

    @adds.setter
    def adds(self, x):
        self.add(x)
