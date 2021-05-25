class Local_Definitions:
    """Local Definitions

    Allows components, and inventory-items to be defined within the POA&M
for circumstances where no OSCAL-based SSP exists, or is not delivered
with the POA&M.

    Attributes:
        prose (str):Default value holder for raw data in texts

        component (BY_KEY):

        inventory_item (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-poam",
        "oscal-metadata",
        "oscal-implementation-common",
        "oscal-assessment-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "component",
        "inventory_item",
        "remarks",
    ]

    def __init__(
        self,
        use_name='local-definitions',
        prose=None,
        component=None,
        inventory_item=None,
        remarks=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._component = None
        self.component = \
            component
        self._inventory_item = None
        self.inventory_item = \
            inventory_item
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if component is None:
            self.component = []
        if inventory_item is None:
            self.inventory_item = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            component=obj.get(
                'component',
                None),
            inventory_item=obj.get(
                'inventory_item',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.component = \
            obj.get('components')
        newcls.inventory_item = \
            obj.get('inventory_items')
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
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, x):
        self._remarks = x

    @property
    def component(self):
        return self._component

    @component.setter
    def component(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._component):
            self._component = []
        if bool(x):
            if x != self._component:
                self._component += list(x)

    @property
    def components(self):
        return self._component

    @components.setter
    def components(self, x):
        self.component(x)

    @property
    def inventory_item(self):
        return self._inventory_item

    @inventory_item.setter
    def inventory_item(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._inventory_item):
            self._inventory_item = []
        if bool(x):
            if x != self._inventory_item:
                self._inventory_item += list(x)

    @property
    def inventory_items(self):
        return self._inventory_item

    @inventory_items.setter
    def inventory_items(self, x):
        self.inventory_item(x)
