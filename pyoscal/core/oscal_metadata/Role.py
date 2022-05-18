class Role:
    """Role

    Defines a function assumed or expected to be assumed by a party in a
specific situation.

    Attributes:
        id (token):A unique identifier for a specific role instance.
This identifier's uniqueness is document scoped and is
intended to be consistent for the same role across minor
revisions of the document.

        prose (str):Default value holder for raw data in texts

        title (markup-line):A name given to the role, which may be
used by a tool for display and navigation.

        short_name (str):A short common name, abbreviation, or
acronym for the role.

        description (markup-multiline):A summary of the role's
purpose and associated responsibilities.

        oscal_property (ARRAY):

        link (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "id",
    ]
    subcomponents = [
        "prose",
        "title",
        "short_name",
        "description",
        "oscal_property",
        "link",
        "remarks",
    ]

    def __init__(
        self,
        id,
        title,
        use_name='role',
        prose=None,
        short_name=None,
        description=None,
        oscal_property=None,
        link=None,
        remarks=None,
    ):
        self._id = None
        self.id = \
            id
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
            id=obj.get(
                'id',
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
    def id(self):
        """A unique identifier for a specific role instance. This identifier's
        uniqueness is document scoped and is intended to be consistent for
        the same role across minor revisions of the document.
        """
        return self._id

    @id.setter
    def id(self, x):
        self._id = x

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
        """A name given to the role, which may be used by a tool for display
        and navigation.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def short_name(self):
        """A short common name, abbreviation, or acronym for the role.
        """
        return self._short_name

    @short_name.setter
    def short_name(self, x):
        self._short_name = x

    @property
    def description(self):
        """A summary of the role's purpose and associated responsibilities.
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
