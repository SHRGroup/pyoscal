class Set_Parameter:
    """Parameter Setting

    A parameter setting, to be propagated to points of insertion

    Attributes:
        param_id (token):Indicates the value of the 'id' flag on a
target parameter; i.e. which parameter to set

        oscal_class (token):A textual label that provides a
characterization of the parameter.

        depends_on (str):

        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

        label (markup-line):A short, placeholder name for the
parameter, which can be used as a substitute for a

        usage (markup-multiline):Describes the purpose and use of a
parameter

        constraint (ARRAY):

        guideline (ARRAY):

        value (ARRAY):

        select (str):

    """

    contexts = [
        "oscal-profile",
        "oscal-metadata",
        "oscal-catalog-common",
    ]
    parameters = [
        "param_id",
        "oscal_class",
        "depends_on",
    ]
    subcomponents = [
        "prose",
        "oscal_property",
        "link",
        "label",
        "usage",
        "constraint",
        "guideline",
        "value",
        "select",
    ]

    def __init__(
        self,
        param_id,
        use_name='set-parameter',
        oscal_class=None,
        depends_on=None,
        prose=None,
        oscal_property=None,
        link=None,
        label=None,
        usage=None,
        constraint=None,
        guideline=None,
        value=None,
        select=None,
    ):
        self._param_id = None
        self.param_id = \
            param_id
        self._oscal_class = None
        self.oscal_class = \
            oscal_class
        self._depends_on = None
        self.depends_on = \
            depends_on
        self._prose = None
        self.prose = \
            prose
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._label = None
        self.label = \
            label
        self._usage = None
        self.usage = \
            usage
        self._constraint = None
        self.constraint = \
            constraint
        self._guideline = None
        self.guideline = \
            guideline
        self._value = None
        self.value = \
            value
        self._select = None
        self.select = \
            select
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if constraint is None:
            self.constraint = []
        if guideline is None:
            self.guideline = []
        if value is None:
            self.value = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            param_id=obj.get(
                'param_id',
                None),
            oscal_class=obj.get(
                'oscal_class',
                None),
            depends_on=obj.get(
                'depends_on',
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
            label=obj.get(
                'label',
                None),
            usage=obj.get(
                'usage',
                None),
            constraint=obj.get(
                'constraint',
                None),
            guideline=obj.get(
                'guideline',
                None),
            value=obj.get(
                'value',
                None),
            select=obj.get(
                'select',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.constraint = \
            obj.get('constraints')
        newcls.guideline = \
            obj.get('guidelines')
        newcls.value = \
            obj.get('values')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def param_id(self):
        """Indicates the value of the 'id' flag on a target parameter; i.e.
        which parameter to set
        """
        return self._param_id

    @param_id.setter
    def param_id(self, x):
        self._param_id = x

    @property
    def oscal_class(self):
        """A textual label that provides a characterization of the parameter.
        """
        return self._oscal_class

    @oscal_class.setter
    def oscal_class(self, x):
        self._oscal_class = x

    @property
    def depends_on(self):
        return self._depends_on

    @depends_on.setter
    def depends_on(self, x):
        self._depends_on = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def label(self):
        """A short, placeholder name for the parameter, which can be used as a
        substitute for a
        """
        return self._label

    @label.setter
    def label(self, x):
        self._label = x

    @property
    def usage(self):
        """Describes the purpose and use of a parameter
        """
        return self._usage

    @usage.setter
    def usage(self, x):
        self._usage = x

    @property
    def select(self):
        return self._select

    @select.setter
    def select(self, x):
        self._select = x

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
    def constraint(self):
        return self._constraint

    @constraint.setter
    def constraint(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._constraint):
            self._constraint = []
        if bool(x):
            if x != self._constraint:
                self._constraint += list(x)

    @property
    def constraints(self):
        return self._constraint

    @constraints.setter
    def constraints(self, x):
        self.constraint(x)

    @property
    def guideline(self):
        return self._guideline

    @guideline.setter
    def guideline(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._guideline):
            self._guideline = []
        if bool(x):
            if x != self._guideline:
                self._guideline += list(x)

    @property
    def guidelines(self):
        return self._guideline

    @guidelines.setter
    def guidelines(self, x):
        self.guideline(x)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._value):
            self._value = []
        if bool(x):
            if x != self._value:
                self._value += list(x)

    @property
    def values(self):
        return self._value

    @values.setter
    def values(self, x):
        self.value(x)
