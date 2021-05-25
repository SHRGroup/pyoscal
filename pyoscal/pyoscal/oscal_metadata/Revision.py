class Revision:
    """Revision History Entry

    An entry in a sequential list of revisions to the containing document
in reverse chronological order (i.e., most recent previous revision
first).

    Attributes:
        prose (str):Default value holder for raw data in texts

        title (markup-line):A name given to the document revision,
which may be used by a tool for display and navigation.

        published (str):

        last_modified (str):

        version (str):

        oscal_version (str):

        oscal_property (ARRAY):

        link (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "title",
        "published",
        "last_modified",
        "version",
        "oscal_version",
        "oscal_property",
        "link",
        "remarks",
    ]

    def __init__(
        self,
        use_name='revision',
        prose=None,
        title=None,
        published=None,
        last_modified=None,
        version=None,
        oscal_version=None,
        oscal_property=None,
        link=None,
        remarks=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._title = None
        self.title = \
            title
        self._published = None
        self.published = \
            published
        self._last_modified = None
        self.last_modified = \
            last_modified
        self._version = None
        self.version = \
            version
        self._oscal_version = None
        self.oscal_version = \
            oscal_version
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
            prose=obj.get(
                'prose',
                None),
            title=obj.get(
                'title',
                None),
            published=obj.get(
                'published',
                None),
            last_modified=obj.get(
                'last_modified',
                None),
            version=obj.get(
                'version',
                None),
            oscal_version=obj.get(
                'oscal_version',
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
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def title(self):
        """A name given to the document revision, which may be used by a tool
        for display and navigation.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def published(self):
        return self._published

    @published.setter
    def published(self, x):
        self._published = x

    @property
    def last_modified(self):
        return self._last_modified

    @last_modified.setter
    def last_modified(self, x):
        self._last_modified = x

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, x):
        self._version = x

    @property
    def oscal_version(self):
        return self._oscal_version

    @oscal_version.setter
    def oscal_version(self, x):
        self._oscal_version = x

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
