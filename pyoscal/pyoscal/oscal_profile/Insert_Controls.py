class Insert_Controls:
    """Select controls

    Specifies which controls to use in the containing context.

    Attributes:
        order (token):A designation of how a selection of controls
in a profile is to be ordered.

        prose (str):Default value holder for raw data in texts

        exclude_controls (ARRAY):

        include_all (str):

        include_controls (ARRAY):

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
        "order",
    ]
    subcomponents = [
        "prose",
        "exclude_controls",
        "include_all",
        "include_controls",
    ]

    def __init__(
        self,
        include_all,
        include_controls,
        use_name='insert-controls',
        order=None,
        prose=None,
        exclude_controls=None,
    ):
        self._order = None
        self.order = \
            order
        self._prose = None
        self.prose = \
            prose
        self._exclude_controls = None
        self.exclude_controls = \
            exclude_controls
        self._include_all = None
        self.include_all = \
            include_all
        self._include_controls = None
        self.include_controls = \
            include_controls
        self.use_name = use_name
        if exclude_controls is None:
            self.exclude_controls = []
        if include_controls is None:
            self.include_controls = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            order=obj.get(
                'order',
                None),
            prose=obj.get(
                'prose',
                None),
            exclude_controls=obj.get(
                'exclude_controls',
                None),
            include_all=obj.get(
                'include_all',
                None),
            include_controls=obj.get(
                'include_controls',
                None),
        )
        newcls.exclude_controls = \
            obj.get('exclude_controls')
        newcls.include_controls = \
            obj.get('include_controls')
        return newcls

    @property
    def order(self):
        """A designation of how a selection of controls in a profile is to be
        ordered.
        """
        return self._order

    @order.setter
    def order(self, x):
        self._order = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def include_all(self):
        return self._include_all

    @include_all.setter
    def include_all(self, x):
        self._include_all = x

    @property
    def exclude_controls(self):
        return self._exclude_controls

    @exclude_controls.setter
    def exclude_controls(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._exclude_controls):
            self._exclude_controls = []
        if bool(x):
            if x != self._exclude_controls:
                self._exclude_controls += list(x)

    @property
    def include_controls(self):
        return self._include_controls

    @include_controls.setter
    def include_controls(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._include_controls):
            self._include_controls = []
        if bool(x):
            if x != self._include_controls:
                self._include_controls += list(x)
