class System_User:
    """System User

    A type of user that interacts with the system based on an associated
role.

    Attributes:
        uuid (uuid):The unique identifier for the user class.

        prose (str):Default value holder for raw data in texts

        title (markup-line):A name given to the user, which may be
used by a tool for display and navigation.

        short_name (str):A short common name, abbreviation, or
acronym for the user.

        description (markup-multiline):A summary of the user's
purpose within the system.

        oscal_property (ARRAY):

        link (ARRAY):

        role_id (ARRAY):

        authorized_privilege (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-implementation-common",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "title",
        "short_name",
        "description",
        "oscal_property",
        "link",
        "role_id",
        "authorized_privilege",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        use_name='system-user',
        prose=None,
        title=None,
        short_name=None,
        description=None,
        oscal_property=None,
        link=None,
        role_id=None,
        authorized_privilege=None,
        remarks=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._prose = None
        self.prose = \
            prose
        self._title = None
        self.title = \
            title
        self._short_name = None
        self.short_name = \
            short_name
        self._description = None
        self.description = \
            description
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._role_id = None
        self.role_id = \
            role_id
        self._authorized_privilege = None
        self.authorized_privilege = \
            authorized_privilege
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if role_id is None:
            self.role_id = []
        if authorized_privilege is None:
            self.authorized_privilege = []

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
            title=obj.get(
                'title',
                None),
            short_name=obj.get(
                'short_name',
                None),
            description=obj.get(
                'description',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            role_id=obj.get(
                'role_id',
                None),
            authorized_privilege=obj.get(
                'authorized_privilege',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.role_id = \
            obj.get('role_ids')
        newcls.authorized_privilege = \
            obj.get('authorized_privileges')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """The unique identifier for the user class.
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
    def title(self):
        """A name given to the user, which may be used by a tool for display
        and navigation.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def short_name(self):
        """A short common name, abbreviation, or acronym for the user.
        """
        return self._short_name

    @short_name.setter
    def short_name(self, x):
        self._short_name = x

    @property
    def description(self):
        """A summary of the user's purpose within the system.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

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
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._role_id):
            self._role_id = []
        if bool(x):
            if x != self._role_id:
                self._role_id += list(x)

    @property
    def role_ids(self):
        return self._role_id

    @role_ids.setter
    def role_ids(self, x):
        self.role_id(x)

    @property
    def authorized_privilege(self):
        return self._authorized_privilege

    @authorized_privilege.setter
    def authorized_privilege(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._authorized_privilege):
            self._authorized_privilege = []
        if bool(x):
            if x != self._authorized_privilege:
                self._authorized_privilege += list(x)

    @property
    def authorized_privileges(self):
        return self._authorized_privilege

    @authorized_privileges.setter
    def authorized_privileges(self, x):
        self.authorized_privilege(x)


class User(System_User):
    def __init__(self, **kw):
        super(User, self).__init__(**kw)
        self.use_name = 'user'
