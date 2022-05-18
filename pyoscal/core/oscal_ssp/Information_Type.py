class Information_Type:
    """Information Type

    Contains details about one information type that is stored, processed,
or transmitted by the system, such as privacy information, and those
defined in

    Attributes:
        uuid (uuid):A globally unique identifier that can be used to
reference this information type entry elsewhere in an OSCAL
document. A UUID should be consistently used for a given
resource across revisions of the document.

        prose (str):Default value holder for raw data in texts

        title (markup-line):A human readable name for the
information type. This title should be meaningful within the
context of the system.

        description (markup-multiline):A summary of how this
information type is used within the system.

        categorization (ARRAY):A set of information type identifiers
qualified by the given identification

        oscal_property (ARRAY):

        link (ARRAY):

        confidentiality_impact (str):The expected level of impact
resulting from the unauthorized disclosure of the described
information.

        integrity_impact (str):The expected level of impact
resulting from the unauthorized modification of the
described information.

        availability_impact (str):The expected level of impact
resulting from the disruption of access to or use of the
described information or the information system.

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
        "description",
        "categorization",
        "oscal_property",
        "link",
        "confidentiality_impact",
        "integrity_impact",
        "availability_impact",
    ]

    def __init__(
        self,
        title,
        description,
        confidentiality_impact,
        integrity_impact,
        availability_impact,
        use_name='information-type',
        uuid=None,
        prose=None,
        categorization=None,
        oscal_property=None,
        link=None,
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
        self._categorization = None
        self.categorization = \
            categorization
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._confidentiality_impact = None
        self.confidentiality_impact = \
            confidentiality_impact
        self._integrity_impact = None
        self.integrity_impact = \
            integrity_impact
        self._availability_impact = None
        self.availability_impact = \
            availability_impact
        self.use_name = use_name
        if categorization is None:
            self.categorization = []
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
            description=obj.get(
                'description',
                None),
            categorization=obj.get(
                'categorization',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            confidentiality_impact=obj.get(
                'confidentiality_impact',
                None),
            integrity_impact=obj.get(
                'integrity_impact',
                None),
            availability_impact=obj.get(
                'availability_impact',
                None),
        )
        newcls.categorization = \
            obj.get('categorizations')
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
        information type entry elsewhere in an OSCAL document. A UUID should
        be consistently used for a given resource across revisions of the
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
        """A human readable name for the information type. This title should be
        meaningful within the context of the system.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def description(self):
        """A summary of how this information type is used within the system.
        """
        return self._description

    @description.setter
    def description(self, x):
        self._description = x

    @property
    def confidentiality_impact(self):
        """The expected level of impact resulting from the unauthorized
        disclosure of the described information.
        """
        return self._confidentiality_impact

    @confidentiality_impact.setter
    def confidentiality_impact(self, x):
        self._confidentiality_impact = x

    @property
    def integrity_impact(self):
        """The expected level of impact resulting from the unauthorized
        modification of the described information.
        """
        return self._integrity_impact

    @integrity_impact.setter
    def integrity_impact(self, x):
        self._integrity_impact = x

    @property
    def availability_impact(self):
        """The expected level of impact resulting from the disruption of access
        to or use of the described information or the information system.
        """
        return self._availability_impact

    @availability_impact.setter
    def availability_impact(self, x):
        self._availability_impact = x

    @property
    def categorization(self):
        """A set of information type identifiers qualified by the given
        identification
        """
        return self._categorization

    @categorization.setter
    def categorization(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._categorization):
            self._categorization = []
        if bool(x):
            if x != self._categorization:
                self._categorization += list(x)

    @property
    def categorizations(self):
        return self._categorization

    @categorizations.setter
    def categorizations(self, x):
        self.categorization(x)

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
