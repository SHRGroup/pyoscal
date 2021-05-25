class Responsible_Party:
    """Responsible Party

    A reference to a set of organizations or persons that have
responsibility for performing a referenced role in the context of the
containing object.

    Attributes:
        role_id (NCName):The role that the party is responsible for.

        prose (str):Default value holder for raw data in texts

        party_uuid (ARRAY):

        oscal_property (ARRAY):

        link (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "role_id",
    ]
    subcomponents = [
        "prose",
        "party_uuid",
        "oscal_property",
        "link",
        "remarks",
    ]

    def __init__(
        self,
        role_id,
        party_uuid,
        use_name='responsible-party',
        prose=None,
        oscal_property=None,
        link=None,
        remarks=None,
    ):
        self._role_id = None
        self.role_id = \
            role_id
        self._prose = None
        self.prose = \
            prose
        self._party_uuid = None
        self.party_uuid = \
            party_uuid
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if party_uuid is None:
            self.party_uuid = []
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            role_id=obj.get(
                'role_id',
                None),
            prose=obj.get(
                'prose',
                None),
            party_uuid=obj.get(
                'party_uuid',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.party_uuid = \
            obj.get('party_uuids')
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def role_id(self):
        """The role that the party is responsible for.
        """
        return self._role_id

    @role_id.setter
    def role_id(self, x):
        self._role_id = x

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
    def party_uuid(self):
        return self._party_uuid

    @party_uuid.setter
    def party_uuid(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._party_uuid):
            self._party_uuid = []
        if bool(x):
            if x != self._party_uuid:
                self._party_uuid += list(x)

    @property
    def party_uuids(self):
        return self._party_uuid

    @party_uuids.setter
    def party_uuids(self, x):
        self.party_uuid(x)

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
