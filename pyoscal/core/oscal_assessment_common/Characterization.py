class Characterization:
    """Characterization

    A collection of descriptive data about the containing object from a
specific origin.

    Attributes:
        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

        origin (str):

        facet (ARRAY):An individual characteristic that is part of a
larger set produced by the same actor.

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
    ]
    subcomponents = [
        "prose",
        "oscal_property",
        "link",
        "origin",
        "facet",
    ]

    def __init__(
        self,
        origin,
        facet,
        use_name='characterization',
        prose=None,
        oscal_property=None,
        link=None,
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
        self._origin = None
        self.origin = \
            origin
        self._facet = None
        self.facet = \
            facet
        self.use_name = use_name
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if facet is None:
            self.facet = []

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
            origin=obj.get(
                'origin',
                None),
            facet=obj.get(
                'facet',
                None),
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.facet = \
            obj.get('facets')
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
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, x):
        self._origin = x

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
    def facet(self):
        """An individual characteristic that is part of a larger set produced
        by the same actor.
        """
        return self._facet

    @facet.setter
    def facet(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._facet):
            self._facet = []
        if bool(x):
            if x != self._facet:
                self._facet += list(x)

    @property
    def facets(self):
        return self._facet

    @facets.setter
    def facets(self, x):
        self.facet(x)
