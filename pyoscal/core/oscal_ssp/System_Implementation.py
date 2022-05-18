class System_Implementation:
    """System Implementation

    Provides information as to how the system is implemented.

    Attributes:
        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

        leveraged_authorization (ARRAY):A description of another
authorized system from which this system inherits
capabilities that satisfy security requirements. Another
term for this concept is a

        user (ARRAY):

        component (ARRAY):

        inventory_item (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-ssp",
        "oscal-metadata",
        "oscal-implementation-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "oscal_property",
        "link",
        "leveraged_authorization",
        "user",
        "component",
        "inventory_item",
        "remarks",
    ]

    def __init__(
        self,
        user,
        component,
        use_name='system-implementation',
        prose=None,
        oscal_property=None,
        link=None,
        leveraged_authorization=None,
        inventory_item=None,
        remarks=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._leveraged_authorization = None
        self.leveraged_authorization = \
            leveraged_authorization
        self._user = None
        self.user = \
            user
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
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if leveraged_authorization is None:
            self.leveraged_authorization = []
        if user is None:
            self.user = []
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
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            leveraged_authorization=obj.get(
                'leveraged_authorization',
                None),
            user=obj.get(
                'user',
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
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.leveraged_authorization = \
            obj.get('leveraged_authorizations')
        newcls.user = \
            obj.get('users')
        newcls.component = \
            obj.get('components')
        newcls.inventory_item = \
            obj.get('inventory_items')
        newcls.oscal_property = \
            obj.get('prop')
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
    def oscal_property(self):
        return self._oscal_property

    @oscal_property.setter
    def oscal_property(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._oscal_property):
            self._oscal_property = []
        if bool(x):
            if x != self._oscal_property:
                self._oscal_property += list(x)

    @property
    def props(self):
        return self._oscal_property

    @props.setter
    def props(self, x):
        self.oscal_property(x)

    @property
    def prop(self):
        return self._oscal_property

    @prop.setter
    def prop(self, x):
        self.oscal_property(x)

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._link):
            self._link = []
        if bool(x):
            if x != self._link:
                self._link += list(x)

    @property
    def links(self):
        return self._link

    @links.setter
    def links(self, x):
        self.link(x)

    @property
    def leveraged_authorization(self):
        """A description of another authorized system from which this system
        inherits capabilities that satisfy security requirements. Another
        term for this concept is a
        """
        return self._leveraged_authorization

    @leveraged_authorization.setter
    def leveraged_authorization(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._leveraged_authorization):
            self._leveraged_authorization = []
        if bool(x):
            if x != self._leveraged_authorization:
                self._leveraged_authorization += list(x)

    @property
    def leveraged_authorizations(self):
        return self._leveraged_authorization

    @leveraged_authorizations.setter
    def leveraged_authorizations(self, x):
        self.leveraged_authorization(x)

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
