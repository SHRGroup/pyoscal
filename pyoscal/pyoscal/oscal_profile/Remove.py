class Remove:
    """Removal

    Specifies objects to be removed from a control based on specific
aspects of the object that must all match.

    Attributes:
        by_name (token):Identify items to remove by matching their
assigned name

        by_class (token):Identify items to remove by matching their

        by_id (token):Identify items to remove indicated by their

        by_item_name (token):Identify items to remove by the name of
the item's information element name, e.g.

        by_ns (token):Identify items to remove by the item's

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
        "by_name",
        "by_class",
        "by_id",
        "by_item_name",
        "by_ns",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        use_name='remove',
        by_name=None,
        by_class=None,
        by_id=None,
        by_item_name=None,
        by_ns=None,
        prose=None,
    ):
        self._by_name = None
        self.by_name = \
            by_name
        self._by_class = None
        self.by_class = \
            by_class
        self._by_id = None
        self.by_id = \
            by_id
        self._by_item_name = None
        self.by_item_name = \
            by_item_name
        self._by_ns = None
        self.by_ns = \
            by_ns
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            by_name=obj.get(
                'by_name',
                None),
            by_class=obj.get(
                'by_class',
                None),
            by_id=obj.get(
                'by_id',
                None),
            by_item_name=obj.get(
                'by_item_name',
                None),
            by_ns=obj.get(
                'by_ns',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def by_name(self):
        """Identify items to remove by matching their assigned name
        """
        return self._by_name

    @by_name.setter
    def by_name(self, x):
        self._by_name = x

    @property
    def by_class(self):
        """Identify items to remove by matching their
        """
        return self._by_class

    @by_class.setter
    def by_class(self, x):
        self._by_class = x

    @property
    def by_id(self):
        """Identify items to remove indicated by their
        """
        return self._by_id

    @by_id.setter
    def by_id(self, x):
        self._by_id = x

    @property
    def by_item_name(self):
        """Identify items to remove by the name of the item's information
        element name, e.g.
        """
        return self._by_item_name

    @by_item_name.setter
    def by_item_name(self, x):
        self._by_item_name = x

    @property
    def by_ns(self):
        """Identify items to remove by the item's
        """
        return self._by_ns

    @by_ns.setter
    def by_ns(self, x):
        self._by_ns = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
