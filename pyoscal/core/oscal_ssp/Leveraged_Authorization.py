class Leveraged_Authorization:
    """Leveraged Authorization

    A description of another authorized system from which this system
inherits capabilities that satisfy security requirements. Another term
for this concept is a

    Attributes:
        uuid (uuid):A globally unique identifier that can be used to
reference this leveraged authorization entry elsewhere in an
OSCAL document. A UUID should be consistently used for a
given resource across revisions of the document.

        prose (str):Default value holder for raw data in texts

        title (markup-line):A human readable name for the leveraged
authorization in the context of the system.

        oscal_property (ARRAY):

        link (ARRAY):

        party_uuid (uuid):A reference to the party that manages the
leveraged system.

        date_authorized (str):

        remarks (str):

    """

    contexts = [
        "oscal-ssp",
        "oscal-metadata",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "title",
        "oscal_property",
        "link",
        "party_uuid",
        "date_authorized",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        title,
        party_uuid,
        date_authorized,
        use_name='leveraged-authorization',
        prose=None,
        oscal_property=None,
        link=None,
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
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._party_uuid = None
        self.party_uuid = \
            party_uuid
        self._date_authorized = None
        self.date_authorized = \
            date_authorized
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []

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
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            party_uuid=obj.get(
                'party_uuid',
                None),
            date_authorized=obj.get(
                'date_authorized',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """A globally unique identifier that can be used to reference this
        leveraged authorization entry elsewhere in an OSCAL document. A UUID
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
    def title(self):
        """A human readable name for the leveraged authorization in the context
        of the system.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def party_uuid(self):
        """A reference to the party that manages the leveraged system.
        """
        return self._party_uuid

    @party_uuid.setter
    def party_uuid(self, x):
        self._party_uuid = x

    @property
    def date_authorized(self):
        return self._date_authorized

    @date_authorized.setter
    def date_authorized(self, x):
        self._date_authorized = x

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
