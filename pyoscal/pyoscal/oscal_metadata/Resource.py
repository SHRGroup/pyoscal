class Resource:
    """Resource

    A resource associated with content in the containing document. A
resource may be directly included in the document base64 encoded or
may point to one or more equivalent internet resources.

    Attributes:
        uuid (uuid):A globally unique identifier that can be used to
reference this defined resource elsewhere in an OSCAL
document. A UUID should be consistently used for a given
resource across revisions of the document.

        prose (str):Default value holder for raw data in texts

        title (markup-line):A name given to the resource, which may
be used by a tool for display and navigation.

        description (markup-multiline):A short summary of the
resource used to indicate the purpose of the resource.

        oscal_property (ARRAY):

        document_id (ARRAY):

        citation (str):A citation consisting of end note text and
optional structured bibliographic data.

        rlink (ARRAY):A pointer to an external resource with an
optional hash for verification and change detection.

        base64 (base64Binary):The Base64 alphabet in RFC 2045 -
aligned with XSD.

        remarks (str):

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "title",
        "description",
        "oscal_property",
        "document_id",
        "citation",
        "rlink",
        "base64",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        use_name='resource',
        prose=None,
        title=None,
        description=None,
        oscal_property=None,
        document_id=None,
        citation=None,
        rlink=None,
        base64=None,
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
        self._description = None
        self.description = \
            description
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._document_id = None
        self.document_id = \
            document_id
        self._citation = None
        self.citation = \
            citation
        self._rlink = None
        self.rlink = \
            rlink
        self._base64 = None
        self.base64 = \
            base64
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if document_id is None:
            self.document_id = []
        if rlink is None:
            self.rlink = []

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
            description=obj.get(
                'description',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            document_id=obj.get(
                'document_id',
                None),
            citation=obj.get(
                'citation',
                None),
            rlink=obj.get(
                'rlink',
                None),
            base64=obj.get(
                'base64',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.document_id = \
            obj.get('document_ids')
        newcls.rlink = \
            obj.get('rlinks')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """A globally unique identifier that can be used to reference this
        defined resource elsewhere in an OSCAL document. A UUID should be
        consistently used for a given resource across revisions of the
        document.
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
        """A name given to the resource, which may be used by a tool for
        display and navigation.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A short summary of the resource used to indicate the purpose of the
        resource.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def citation(self):
        """A citation consisting of end note text and optional structured
        bibliographic data.
        """
        return self._citation

    @citation.setter
    def citation(self, x):
        self._citation = x

    @property
    def base64(self):
        """The Base64 alphabet in RFC 2045 - aligned with XSD.
        """
        return self._base64

    @base64.setter
    def base64(self, x):
        self._base64 = x

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
    def rlink(self):
        """A pointer to an external resource with an optional hash for
        verification and change detection.
        """
        return self._rlink

    @rlink.setter
    def rlink(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._rlink):
            self._rlink = []
        if bool(x):
            if x != self._rlink:
                self._rlink += list(x)

    @property
    def rlinks(self):
        return self._rlink

    @rlinks.setter
    def rlinks(self, x):
        self.rlink(x)
