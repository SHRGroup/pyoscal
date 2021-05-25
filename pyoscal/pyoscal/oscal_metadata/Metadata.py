class Metadata:
    """Publication metadata

    Provides information about the publication and availability of the
containing document.

    Attributes:
        prose (str):Default value holder for raw data in texts

        title (markup-line):A name given to the document, which may
be used by a tool for display and navigation.

        published (str):

        last_modified (str):

        version (str):

        oscal_version (str):

        revision (ARRAY):

        document_id (ARRAY):

        oscal_property (ARRAY):

        link (ARRAY):

        role (ARRAY):

        location (ARRAY):

        party (ARRAY):

        responsible_party (BY_KEY):

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
        "revision",
        "document_id",
        "oscal_property",
        "link",
        "role",
        "location",
        "party",
        "responsible_party",
        "remarks",
    ]

    def __init__(
        self,
        title,
        last_modified,
        version,
        oscal_version,
        use_name='metadata',
        prose=None,
        published=None,
        revision=None,
        document_id=None,
        oscal_property=None,
        link=None,
        role=None,
        location=None,
        party=None,
        responsible_party=None,
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
        self._revision = None
        self.revision = \
            revision
        self._document_id = None
        self.document_id = \
            document_id
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._role = None
        self.role = \
            role
        self._location = None
        self.location = \
            location
        self._party = None
        self.party = \
            party
        self._responsible_party = None
        self.responsible_party = \
            responsible_party
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if revision is None:
            self.revision = []
        if document_id is None:
            self.document_id = []
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if role is None:
            self.role = []
        if location is None:
            self.location = []
        if party is None:
            self.party = []
        if responsible_party is None:
            self.responsible_party = []

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
            revision=obj.get(
                'revision',
                None),
            document_id=obj.get(
                'document_id',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            role=obj.get(
                'role',
                None),
            location=obj.get(
                'location',
                None),
            party=obj.get(
                'party',
                None),
            responsible_party=obj.get(
                'responsible_party',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.revision = \
            obj.get('revisions')
        newcls.document_id = \
            obj.get('document_ids')
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.role = \
            obj.get('roles')
        newcls.location = \
            obj.get('locations')
        newcls.party = \
            obj.get('parties')
        newcls.responsible_party = \
            obj.get('responsible_parties')
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
        """A name given to the document, which may be used by a tool for
        display and navigation.
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
    def revision(self):
        return self._revision

    @revision.setter
    def revision(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._revision):
            self._revision = []
        if bool(x):
            if x != self._revision:
                self._revision += list(x)

    @property
    def revisions(self):
        return self._revision

    @revisions.setter
    def revisions(self, x):
        self.revision(x)

    @property
    def document_id(self):
        return self._document_id

    @document_id.setter
    def document_id(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._document_id):
            self._document_id = []
        if bool(x):
            if x != self._document_id:
                self._document_id += list(x)

    @property
    def document_ids(self):
        return self._document_id

    @document_ids.setter
    def document_ids(self, x):
        self.document_id(x)

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
    def role(self):
        return self._role

    @role.setter
    def role(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._role):
            self._role = []
        if bool(x):
            if x != self._role:
                self._role += list(x)

    @property
    def roles(self):
        return self._role

    @roles.setter
    def roles(self, x):
        self.role(x)

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._location):
            self._location = []
        if bool(x):
            if x != self._location:
                self._location += list(x)

    @property
    def locations(self):
        return self._location

    @locations.setter
    def locations(self, x):
        self.location(x)

    @property
    def party(self):
        return self._party

    @party.setter
    def party(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._party):
            self._party = []
        if bool(x):
            if x != self._party:
                self._party += list(x)

    @property
    def parties(self):
        return self._party

    @parties.setter
    def parties(self, x):
        self.party(x)

    @property
    def responsible_party(self):
        return self._responsible_party

    @responsible_party.setter
    def responsible_party(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._responsible_party):
            self._responsible_party = []
        if bool(x):
            if x != self._responsible_party:
                self._responsible_party += list(x)

    @property
    def responsible_parties(self):
        return self._responsible_party

    @responsible_parties.setter
    def responsible_parties(self, x):
        self.responsible_party(x)
