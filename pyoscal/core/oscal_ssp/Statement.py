class Statement:
    """Specific Control Statement

    Identifies which statements within a control are addressed.

    Attributes:
        statement_id (str):

        uuid (uuid):A globally unique identifier that can be used to
reference this control statement entry elsewhere in an OSCAL
document. A UUID should be consistently used for a given
resource across revisions of the document.

        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

        responsible_role (ARRAY):

        by_component (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-ssp",
        "oscal-metadata",
        "oscal-implementation-common",
    ]
    parameters = [
        "statement_id",
        "uuid",
    ]
    subcomponents = [
        "prose",
        "oscal_property",
        "link",
        "responsible_role",
        "by_component",
        "remarks",
    ]

    def __init__(
        self,
        statement_id,
        uuid,
        use_name='statement',
        prose=None,
        oscal_property=None,
        link=None,
        responsible_role=None,
        by_component=None,
        remarks=None,
    ):
        self._statement_id = None
        self.statement_id = \
            statement_id
        self._uuid = None
        self.uuid = \
            uuid
        self._prose = None
        self.prose = \
            prose
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._responsible_role = None
        self.responsible_role = \
            responsible_role
        self._by_component = None
        self.by_component = \
            by_component
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if responsible_role is None:
            self.responsible_role = []
        if by_component is None:
            self.by_component = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            statement_id=obj.get(
                'statement_id',
                None),
            uuid=obj.get(
                'uuid',
                None),
            prose=obj.get(
                'prose',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            responsible_role=obj.get(
                'responsible_role',
                None),
            by_component=obj.get(
                'by_component',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.responsible_role = \
            obj.get('responsible_roles')
        newcls.by_component = \
            obj.get('by_components')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def statement_id(self):
        return self._statement_id

    @statement_id.setter
    def statement_id(self, x):
        self._statement_id = x

    @property
    def uuid(self):
        """A globally unique identifier that can be used to reference this
        control statement entry elsewhere in an OSCAL document. A UUID
        should be consistently used for a given resource across revisions of
        the document.
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
    def responsible_role(self):
        return self._responsible_role

    @responsible_role.setter
    def responsible_role(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._responsible_role):
            self._responsible_role = []
        if bool(x):
            if x != self._responsible_role:
                self._responsible_role += list(x)

    @property
    def responsible_roles(self):
        return self._responsible_role

    @responsible_roles.setter
    def responsible_roles(self, x):
        self.responsible_role(x)

    @property
    def by_component(self):
        return self._by_component

    @by_component.setter
    def by_component(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._by_component):
            self._by_component = []
        if bool(x):
            if x != self._by_component:
                self._by_component += list(x)

    @property
    def by_components(self):
        return self._by_component

    @by_components.setter
    def by_components(self, x):
        self.by_component(x)
