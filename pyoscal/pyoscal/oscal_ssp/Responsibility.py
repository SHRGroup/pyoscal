class Responsibility:
    """Control Implementation Responsibility

    Describes a control implementation responsibility imposed on a
leveraging system.

    Attributes:
        uuid (uuid):A globally unique identifier that can be used to
reference this responsibility entry elsewhere in an OSCAL
document. A UUID should be consistently used for a given
resource across revisions of the document.

        provided_uuid (str):

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):An implementation statement
that describes the aspects of the control or control
statement implementation that a leveraging system must
implement to satisfy the control provided by a leveraged
system.

        oscal_property (ARRAY):

        link (ARRAY):

        responsible_role (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-ssp",
        "oscal-metadata",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
        "provided_uuid",
    ]
    subcomponents = [
        "prose",
        "description",
        "oscal_property",
        "link",
        "responsible_role",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        provided_uuid,
        description,
        use_name='responsibility',
        prose=None,
        oscal_property=None,
        link=None,
        responsible_role=None,
        remarks=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._provided_uuid = None
        self.provided_uuid = \
            provided_uuid
        self._prose = None
        self.prose = \
            prose
        self._description = None
        self.description = \
            description
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._responsible_role = None
        self.responsible_role = \
            responsible_role
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

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid=obj.get(
                'uuid',
                None),
            provided_uuid=obj.get(
                'provided_uuid',
                None),
            prose=obj.get(
                'prose',
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
            responsible_role=obj.get(
                'responsible_role',
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
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """A globally unique identifier that can be used to reference this
        responsibility entry elsewhere in an OSCAL document. A UUID should
        be consistently used for a given resource across revisions of the
        document.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def provided_uuid(self):
        return self._provided_uuid

    @provided_uuid.setter
    def provided_uuid(self, x):
        self._provided_uuid = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def description(self):
        """An implementation statement that describes the aspects of the
        control or control statement implementation that a leveraging system
        must implement to satisfy the control provided by a leveraged
        system.
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
