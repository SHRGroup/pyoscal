class Remove:
    """Removal

    Specifies objects to be removed from a control based on specific
aspects of the object that must all match.

    Attributes:
        name_ref (NCName):Identify items to remove by matching their
assigned name

        class_ref (NCName):Identify items to remove by matching
their

        id_ref (NCName):Identify items to remove indicated by their

        item_name (NCName):Identify items to remove by the name of
the item's information element name, e.g.

        ns_ref (NCName):Identify items to remove by the item's

        prose (str):Default value holder for raw data in texts

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
        "name_ref",
        "class_ref",
        "id_ref",
        "item_name",
        "ns_ref",
    ]
    subcomponents = [
        "prose",
    ]

    def __init__(
        self,
        use_name='remove',
        name_ref=None,
        class_ref=None,
        id_ref=None,
        item_name=None,
        ns_ref=None,
        prose=None,
    ):
        self._name_ref = None
        self.name_ref = \
            name_ref
        self._class_ref = None
        self.class_ref = \
            class_ref
        self._id_ref = None
        self.id_ref = \
            id_ref
        self._item_name = None
        self.item_name = \
            item_name
        self._ns_ref = None
        self.ns_ref = \
            ns_ref
        self._prose = None
        self.prose = \
            prose
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            name_ref=obj.get(
                'name_ref',
                None),
            class_ref=obj.get(
                'class_ref',
                None),
            id_ref=obj.get(
                'id_ref',
                None),
            item_name=obj.get(
                'item_name',
                None),
            ns_ref=obj.get(
                'ns_ref',
                None),
            prose=obj.get(
                'prose',
                None),
        )
        return newcls

    @property
    def name_ref(self):
        """Identify items to remove by matching their assigned name
        """
        return self._name_ref

    @name_ref.setter
    def name_ref(self, x):
        self._name_ref = x

    @property
    def class_ref(self):
        """Identify items to remove by matching their
        """
        return self._class_ref

    @class_ref.setter
    def class_ref(self, x):
        self._class_ref = x

    @property
    def id_ref(self):
        """Identify items to remove indicated by their
        """
        return self._id_ref

    @id_ref.setter
    def id_ref(self, x):
        self._id_ref = x

    @property
    def item_name(self):
        """Identify items to remove by the name of the item's information
        element name, e.g.
        """
        return self._item_name

    @item_name.setter
    def item_name(self, x):
        self._item_name = x

    @property
    def ns_ref(self):
        """Identify items to remove by the item's
        """
        return self._ns_ref

    @ns_ref.setter
    def ns_ref(self, x):
        self._ns_ref = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x
