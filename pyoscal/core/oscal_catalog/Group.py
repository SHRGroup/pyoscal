class Group:
    """Control Group

    A group of controls, or of groups of controls.

    Attributes:
        id (token):A unique identifier for a specific group instance
that can be used to reference the group within this and in
other OSCAL documents. This identifier's uniqueness is
document scoped and is intended to be consistent for the
same group across minor revisions of the document.

        oscal_class (token):A textual label that provides a sub-type
or characterization of the group.

        prose (str):Default value holder for raw data in texts

        title (markup-line):A name given to the group, which may be
used by a tool for display and navigation.

        parameter (ARRAY):

        oscal_property (ARRAY):

        link (ARRAY):

        part (ARRAY):

        group (ARRAY):

        control (ARRAY):

    """

    contexts = [
        "oscal-catalog",
        "oscal-catalog-common",
        "oscal-metadata",
    ]
    parameters = [
        "id",
        "oscal_class",
    ]
    subcomponents = [
        "prose",
        "title",
        "parameter",
        "oscal_property",
        "link",
        "part",
        "group",
        "control",
    ]

    def __init__(
        self,
        title,
        use_name='group',
        id=None,
        oscal_class=None,
        prose=None,
        parameter=None,
        oscal_property=None,
        link=None,
        part=None,
        group=None,
        control=None,
    ):
        self._id = None
        self.id = \
            id
        self._oscal_class = None
        self.oscal_class = \
            oscal_class
        self._prose = None
        self.prose = \
            prose
        self._title = None
        self.title = \
            title
        self._parameter = None
        self.parameter = \
            parameter
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._part = None
        self.part = \
            part
        self._group = None
        self.group = \
            group
        self._control = None
        self.control = \
            control
        self.use_name = use_name
        if parameter is None:
            self.parameter = []
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if part is None:
            self.part = []
        if group is None:
            self.group = []
        if control is None:
            self.control = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            id=obj.get(
                'id',
                None),
            oscal_class=obj.get(
                'oscal_class',
                None),
            prose=obj.get(
                'prose',
                None),
            title=obj.get(
                'title',
                None),
            parameter=obj.get(
                'parameter',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            part=obj.get(
                'part',
                None),
            group=obj.get(
                'group',
                None),
            control=obj.get(
                'control',
                None),
        )
        newcls.parameter = \
            obj.get('params')
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.part = \
            obj.get('parts')
        newcls.group = \
            obj.get('groups')
        newcls.control = \
            obj.get('controls')
        newcls.parameter = \
            obj.get('param')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def id(self):
        """A unique identifier for a specific group instance that can be used
        to reference the group within this and in other OSCAL documents.
        This identifier's uniqueness is document scoped and is intended to
        be consistent for the same group across minor revisions of the
        document.
        """
        return self._id

    @id.setter
    def id(self, x):
        self._id = x

    @property
    def oscal_class(self):
        """A textual label that provides a sub-type or characterization of the
        group.
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
    def title(self):
        """A name given to the group, which may be used by a tool for display
        and navigation.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def parameter(self):
        return self._parameter

    @parameter.setter
    def parameter(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._parameter):
            self._parameter = []
        if bool(x):
            if x != self._parameter:
                self._parameter += list(x)

    @property
    def params(self):
        return self._parameter

    @params.setter
    def params(self, x):
        self.parameter(x)

    @property
    def param(self):
        return self._parameter

    @param.setter
    def param(self, x):
        self.parameter(x)

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
    def part(self):
        return self._part

    @part.setter
    def part(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._part):
            self._part = []
        if bool(x):
            if x != self._part:
                self._part += list(x)

    @property
    def parts(self):
        return self._part

    @parts.setter
    def parts(self, x):
        self.part(x)

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._group):
            self._group = []
        if bool(x):
            if x != self._group:
                self._group += list(x)

    @property
    def groups(self):
        return self._group

    @groups.setter
    def groups(self, x):
        self.group(x)

    @property
    def control(self):
        return self._control

    @control.setter
    def control(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._control):
            self._control = []
        if bool(x):
            if x != self._control:
                self._control += list(x)

    @property
    def controls(self):
        return self._control

    @controls.setter
    def controls(self, x):
        self.control(x)
