class Catalog:
    """Catalog

    A collection of controls.

    Attributes:
        uuid (uuid):A globally unique identifier for this catalog
instance. This UUID should be changed when this document is
revised.

        prose (str):Default value holder for raw data in texts

        metadata (str):

        parameter (ARRAY):

        control (ARRAY):

        group (ARRAY):

        back_matter (str):

    """

    contexts = [
        "oscal-catalog",
        "oscal-catalog-common",
        "oscal-metadata",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "metadata",
        "parameter",
        "control",
        "group",
        "back_matter",
    ]

    def __init__(
        self,
        uuid,
        metadata,
        use_name='catalog',
        prose=None,
        parameter=None,
        control=None,
        group=None,
        back_matter=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._prose = None
        self.prose = \
            prose
        self._metadata = None
        self.metadata = \
            metadata
        self._parameter = None
        self.parameter = \
            parameter
        self._control = None
        self.control = \
            control
        self._group = None
        self.group = \
            group
        self._back_matter = None
        self.back_matter = \
            back_matter
        self.use_name = use_name
        if parameter is None:
            self.parameter = []
        if control is None:
            self.control = []
        if group is None:
            self.group = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid=obj.get(
                'uuid',
                None),
            prose=obj.get(
                'prose',
                None),
            metadata=obj.get(
                'metadata',
                None),
            parameter=obj.get(
                'parameter',
                None),
            control=obj.get(
                'control',
                None),
            group=obj.get(
                'group',
                None),
            back_matter=obj.get(
                'back_matter',
                None),
        )
        newcls.parameter = \
            obj.get('params')
        newcls.control = \
            obj.get('controls')
        newcls.group = \
            obj.get('groups')
        newcls.parameter = \
            obj.get('param')
        return newcls

    @property
    def uuid(self):
        """A globally unique identifier for this catalog instance. This UUID
        should be changed when this document is revised.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, x):
        self._metadata = x

    @property
    def back_matter(self):
        return self._back_matter

    @back_matter.setter
    def back_matter(self, x):
        self._back_matter = x

    @property
    def parameter(self):
        return self._parameter

    @parameter.setter
    def parameter(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._parameter):
            self._parameter = []
        if bool(x):
            if x != self._parameter:
                self._parameter += list(x)

    @property
    def params(self):
        return self._parameter

    @params.setter
    def params(self, x):
        self.parameter(x)

    @property
    def param(self):
        return self._parameter

    @param.setter
    def param(self, x):
        self.parameter(x)

    @property
    def control(self):
        return self._control

    @control.setter
    def control(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._control):
            self._control = []
        if bool(x):
            if x != self._control:
                self._control += list(x)

    @property
    def controls(self):
        return self._control

    @controls.setter
    def controls(self, x):
        self.control(x)

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
