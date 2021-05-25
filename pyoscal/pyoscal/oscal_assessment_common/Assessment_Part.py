class Assessment_Part:
    """Assessment Part

    A partition of an assessment plan or results or a child of another
part.

    Attributes:
        uuid (uuid):A unique identifier for a specific part
instance. This identifier's uniqueness is document scoped
and is intended to be consistent for the same part across
minor revisions of the document.

        name (NCName):A textual label that uniquely identifies the
part's semantic type.

        ns (uri):A namespace qualifying the part's name. This allows
different organizations to associate distinct semantics with
the same name.

        oscal_class (NCName):A textual label that provides a sub-
type or characterization of the part's

        title (markup-line):A name given to the part, which may be
used by a tool for display and navigation.

        oscal_property (ARRAY):

        prose (markup-multiline):Permits multiple paragraphs, lists,
tables etc.

        assessment_part (ARRAY):

        link (ARRAY):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "uuid",
        "name",
        "ns",
        "oscal_class",
    ]
    subcomponents = [
        "title",
        "oscal_property",
        "prose",
        "assessment_part",
        "link",
    ]

    def __init__(
        self,
        name,
        use_name='assessment-part',
        uuid=None,
        ns=None,
        oscal_class=None,
        title=None,
        oscal_property=None,
        prose=None,
        assessment_part=None,
        link=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._name = None
        self.name = \
            name
        self._ns = None
        self.ns = \
            ns
        self._oscal_class = None
        self.oscal_class = \
            oscal_class
        self._title = None
        self.title = \
            title
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._prose = None
        self.prose = \
            prose
        self._assessment_part = None
        self.assessment_part = \
            assessment_part
        self._link = None
        self.link = \
            link
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if assessment_part is None:
            self.assessment_part = []
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
            name=obj.get(
                'name',
                None),
            ns=obj.get(
                'ns',
                None),
            oscal_class=obj.get(
                'oscal_class',
                None),
            title=obj.get(
                'title',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            prose=obj.get(
                'prose',
                None),
            assessment_part=obj.get(
                'assessment_part',
                None),
            link=obj.get(
                'link',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.assessment_part = \
            obj.get('parts')
        newcls.link = \
            obj.get('links')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """A unique identifier for a specific part instance. This identifier's
        uniqueness is document scoped and is intended to be consistent for
        the same part across minor revisions of the document.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def name(self):
        """A textual label that uniquely identifies the part's semantic type.
        """
        return self._name

    @name.setter
    def name(self, x):
        self._name = x

    @property
    def ns(self):
        """A namespace qualifying the part's name. This allows different
        organizations to associate distinct semantics with the same name.
        """
        return self._ns

    @ns.setter
    def ns(self, x):
        self._ns = x

    @property
    def oscal_class(self):
        """A textual label that provides a sub-type or characterization of the
        part's
        """
        return self._oscal_class

    @oscal_class.setter
    def oscal_class(self, x):
        self._oscal_class = x

    @property
    def title(self):
        """A name given to the part, which may be used by a tool for display
        and navigation.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def prose(self):
        """Permits multiple paragraphs, lists, tables etc.
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

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
    def assessment_part(self):
        return self._assessment_part

    @assessment_part.setter
    def assessment_part(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._assessment_part):
            self._assessment_part = []
        if bool(x):
            if x != self._assessment_part:
                self._assessment_part += list(x)

    @property
    def parts(self):
        return self._assessment_part

    @parts.setter
    def parts(self, x):
        self.assessment_part(x)

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


class Part(Assessment_Part):
    def __init__(self, **kw):
        super(Part, self).__init__(**kw)
        self.use_name = 'part'
