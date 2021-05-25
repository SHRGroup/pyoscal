class Confidentiality_Impact:
    """Confidentiality Impact Level

    The expected level of impact resulting from the unauthorized
disclosure of the described information.

    Attributes:
        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

        base (str):

        selected (str):

        adjustment_justification (str):

    """

    contexts = [
        "oscal-ssp",
        "oscal-metadata",
        "oscal-implementation-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "oscal_property",
        "link",
        "base",
        "selected",
        "adjustment_justification",
    ]

    def __init__(
        self,
        base,
        use_name='confidentiality-impact',
        prose=None,
        oscal_property=None,
        link=None,
        selected=None,
        adjustment_justification=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._base = None
        self.base = \
            base
        self._selected = None
        self.selected = \
            selected
        self._adjustment_justification = None
        self.adjustment_justification = \
            adjustment_justification
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
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            base=obj.get(
                'base',
                None),
            selected=obj.get(
                'selected',
                None),
            adjustment_justification=obj.get(
                'adjustment_justification',
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
    def base(self):
        return self._base

    @base.setter
    def base(self, x):
        self._base = x

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, x):
        self._selected = x

    @property
    def adjustment_justification(self):
        return self._adjustment_justification

    @adjustment_justification.setter
    def adjustment_justification(self, x):
        self._adjustment_justification = x

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
