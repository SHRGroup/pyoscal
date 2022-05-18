class Local_Definitions:
    """Local Definitions

    Used to define data objects that are used in the assessment plan, that
do not appear in the referenced SSP.

    Attributes:
        prose (str):Default value holder for raw data in texts

        component (ARRAY):

        inventory_item (ARRAY):

        user (ARRAY):

        objectives_and_methods (ARRAY):

        activity (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-ap",
        "oscal-metadata",
        "oscal-assessment-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "component",
        "inventory_item",
        "user",
        "objectives_and_methods",
        "activity",
        "remarks",
    ]

    def __init__(
        self,
        use_name='local-definitions',
        prose=None,
        component=None,
        inventory_item=None,
        user=None,
        objectives_and_methods=None,
        activity=None,
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
        self._user = None
        self.user = \
            user
        self._objectives_and_methods = None
        self.objectives_and_methods = \
            objectives_and_methods
        self._activity = None
        self.activity = \
            activity
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if component is None:
            self.component = []
        if inventory_item is None:
            self.inventory_item = []
        if user is None:
            self.user = []
        if objectives_and_methods is None:
            self.objectives_and_methods = []
        if activity is None:
            self.activity = []

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
            user=obj.get(
                'user',
                None),
            objectives_and_methods=obj.get(
                'objectives_and_methods',
                None),
            activity=obj.get(
                'activity',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.component = \
            obj.get('components')
        newcls.inventory_item = \
            obj.get('inventory_items')
        newcls.user = \
            obj.get('users')
        newcls.objectives_and_methods = \
            obj.get('objectives_and_methods')
        newcls.activity = \
            obj.get('activities')
        newcls.activity = \
            obj.get('activity')
        newcls.activity = \
            obj.get('activity')
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

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._user):
            self._user = []
        if bool(x):
            if x != self._user:
                self._user += list(x)

    @property
    def users(self):
        return self._user

    @users.setter
    def users(self, x):
        self.user(x)

    @property
    def objectives_and_methods(self):
        return self._objectives_and_methods

    @objectives_and_methods.setter
    def objectives_and_methods(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._objectives_and_methods):
            self._objectives_and_methods = []
        if bool(x):
            if x != self._objectives_and_methods:
                self._objectives_and_methods += list(x)

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._activity):
            self._activity = []
        if bool(x):
            if x != self._activity:
                self._activity += list(x)

    @property
    def activities(self):
        return self._activity

    @activities.setter
    def activities(self, x):
        self.activity(x)
