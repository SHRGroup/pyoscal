class Satisfied:
    """Satisfied Control Implementation Responsibility

    Describes how this system satisfies a responsibility imposed by a
leveraged system.

    Attributes:
        uuid (uuid):A globally unique identifier that can be used to
reference this satisfied entry elsewhere in an OSCAL
document. A UUID should be consistently used for a given
resource across revisions of the document.

        responsibility_uuid (str):

        prose (str):Default value holder for raw data in texts

        description (markup-multiline):An implementation statement
that describes the aspects of a control or control statement
implementation that a leveraging system is implementing
based on a requirement from a leveraged system.

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
        "responsibility_uuid",
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
        responsibility_uuid,
        description,
        use_name='satisfied',
        prose=None,
        oscal_property=None,
        link=None,
        responsible_role=None,
        remarks=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._responsibility_uuid = None
        self.responsibility_uuid = \
            responsibility_uuid
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
            responsibility_uuid=obj.get(
                'responsibility_uuid',
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
        satisfied entry elsewhere in an OSCAL document. A UUID should be
        consistently used for a given resource across revisions of the
        document.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def responsibility_uuid(self):
        return self._responsibility_uuid

    @responsibility_uuid.setter
    def responsibility_uuid(self, x):
        self._responsibility_uuid = x

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
        """An implementation statement that describes the aspects of a control
        or control statement implementation that a leveraging system is
        implementing based on a requirement from a leveraged system.
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
