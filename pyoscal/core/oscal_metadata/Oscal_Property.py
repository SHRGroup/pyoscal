class Oscal_Property:
    """Property

    An attribute, characteristic, or quality of the containing object
expressed as a namespace qualified name/value pair. The value of a
property is a simple scalar value, which may be expressed as a list of
values.

    Attributes:
        name (token):A textual label that uniquely identifies a
specific attribute, characteristic, or quality of the
property's containing object.

        uuid (uuid):A unique identifier that can be used to
reference this property elsewhere in an OSCAL document. A
UUID should be consistently used for a given location across
revisions of the document.

        ns (uri):A namespace qualifying the property's name. This
allows different organizations to associate distinct
semantics with the same name.

        value (string):Indicates the value of the attribute,
characteristic, or quality.

        oscal_class (token):A textual label that provides a sub-type
or characterization of the property's

        prose (str):Default value holder for raw data in texts

        remarks (str):

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "name",
        "uuid",
        "ns",
        "value",
        "oscal_class",
    ]
    subcomponents = [
        "prose",
        "remarks",
    ]

    def __init__(
        self,
        name,
        value,
        use_name='property',
        uuid=None,
        ns=None,
        oscal_class=None,
        prose=None,
        remarks=None,
    ):
        self._name = None
        self.name = \
            name
        self._uuid = None
        self.uuid = \
            uuid
        self._ns = None
        self.ns = \
            ns
        self._value = None
        self.value = \
            value
        self._oscal_class = None
        self.oscal_class = \
            oscal_class
        self._prose = None
        self.prose = \
            prose
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            name=obj.get(
                'name',
                None),
            uuid=obj.get(
                'uuid',
                None),
            ns=obj.get(
                'ns',
                None),
            value=obj.get(
                'value',
                None),
            oscal_class=obj.get(
                'oscal_class',
                None),
            prose=obj.get(
                'prose',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        return newcls

    @property
    def name(self):
        """A textual label that uniquely identifies a specific attribute,
        characteristic, or quality of the property's containing object.
        """
        return self._name

    @name.setter
    def name(self, x):
        self._name = x

    @property
    def uuid(self):
        """A unique identifier that can be used to reference this property
        elsewhere in an OSCAL document. A UUID should be consistently used
        for a given location across revisions of the document.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def ns(self):
        """A namespace qualifying the property's name. This allows different
        organizations to associate distinct semantics with the same name.
        """
        return self._ns

    @ns.setter
    def ns(self, x):
        self._ns = x

    @property
    def value(self):
        """Indicates the value of the attribute, characteristic, or quality.
        """
        return self._value

    @value.setter
    def value(self, x):
        self._value = x

    @property
    def oscal_class(self):
        """A textual label that provides a sub-type or characterization of the
        property's
        """
        return self._oscal_class

    @oscal_class.setter
    def oscal_class(self, x):
        self._oscal_class = x

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


class Prop(Oscal_Property):
    def __init__(self, **kw):
        super(Prop, self).__init__(**kw)
        self.use_name = 'prop'
