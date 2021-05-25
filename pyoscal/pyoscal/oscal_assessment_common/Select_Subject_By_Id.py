class Select_Subject_By_Id:
    """Select Assessment Subject

    Identifies a set of assessment subjects to include/exclude by UUID.

    Attributes:
        uuid_ref (uuid):A pointer to a component, inventory-item,
location, party, user, or resource using it's UUID.

        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid_ref",
    ]
    subcomponents = [
        "prose",
        "oscal_property",
        "link",
        "remarks",
    ]

    def __init__(
        self,
        uuid_ref,
        use_name='select-subject-by-id',
        prose=None,
        oscal_property=None,
        link=None,
        remarks=None,
    ):
        self._uuid_ref = None
        self.uuid_ref = \
            uuid_ref
        self._prose = None
        self.prose = \
            prose
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
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid_ref=obj.get(
                'uuid_ref',
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
    def uuid_ref(self):
        """A pointer to a component, inventory-item, location, party, user, or
        resource using it's UUID.
        """
        return self._uuid_ref

    @uuid_ref.setter
    def uuid_ref(self, x):
        self._uuid_ref = x

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


class Include_Subject(Select_Subject_By_Id):
    def __init__(self, **kw):
        super(Include_Subject, self).__init__(**kw)
        self.use_name = 'include_subject'


class Exclude_Subject(Select_Subject_By_Id):
    def __init__(self, **kw):
        super(Exclude_Subject, self).__init__(**kw)
        self.use_name = 'exclude_subject'
