class Local_Definitions:
    """Local Definitions

    Used to define data objects that are used in the assessment plan, that
do not appear in the referenced SSP.

    Attributes:
        prose (str):Default value holder for raw data in texts

        component (BY_KEY):

        inventory_item (ARRAY):

        user (BY_KEY):

        assessment_assets (str):

        assessment_task (ARRAY):

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
        "component",
        "inventory_item",
        "user",
        "assessment_assets",
        "assessment_task",
    ]

    def __init__(
        self,
        use_name='local-definitions',
        prose=None,
        component=None,
        inventory_item=None,
        user=None,
        assessment_assets=None,
        assessment_task=None,
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
        self._assessment_assets = None
        self.assessment_assets = \
            assessment_assets
        self._assessment_task = None
        self.assessment_task = \
            assessment_task
        self.use_name = use_name
        if component is None:
            self.component = []
        if inventory_item is None:
            self.inventory_item = []
        if user is None:
            self.user = []
        if assessment_task is None:
            self.assessment_task = []

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
            assessment_assets=obj.get(
                'assessment_assets',
                None),
            assessment_task=obj.get(
                'assessment_task',
                None),
        )
        newcls.component = \
            obj.get('components')
        newcls.inventory_item = \
            obj.get('inventory_items')
        newcls.user = \
            obj.get('users')
        newcls.assessment_task = \
            obj.get('tasks')
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
    def assessment_assets(self):
        return self._assessment_assets

    @assessment_assets.setter
    def assessment_assets(self, x):
        self._assessment_assets = x

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
    def assessment_task(self):
        return self._assessment_task

    @assessment_task.setter
    def assessment_task(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._assessment_task):
            self._assessment_task = []
        if bool(x):
            if x != self._assessment_task:
                self._assessment_task += list(x)

    @property
    def tasks(self):
        return self._assessment_task

    @tasks.setter
    def tasks(self, x):
        self.assessment_task(x)
