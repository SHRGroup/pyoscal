class Origin_Actor:
    """Originating Actor

    The actor that produces an observation, a finding, or a risk. One or
more actor type can be used to specify a person that is using a tool.

    Attributes:
        type (token):The kind of actor.

        actor_uuid (uuid):A pointer to the tool or person based on
the associated type.

        role_id (token):For a party, this can optionally be used to
specify the role the actor was performing.

        prose (str):Default value holder for raw data in texts

        oscal_property (ARRAY):

        link (ARRAY):

    """

    contexts = [
        "oscal-assessment-common",
        "oscal-catalog-common",
        "oscal-implementation-common",
    ]
    parameters = [
        "type",
        "actor_uuid",
        "role_id",
    ]
    subcomponents = [
        "prose",
        "oscal_property",
        "link",
    ]

    def __init__(
        self,
        type,
        actor_uuid,
        use_name='origin-actor',
        role_id=None,
        prose=None,
        oscal_property=None,
        link=None,
    ):
        self._type = None
        self.type = \
            type
        self._actor_uuid = None
        self.actor_uuid = \
            actor_uuid
        self._role_id = None
        self.role_id = \
            role_id
        self._prose = None
        self.prose = \
            prose
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
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
            type=obj.get(
                'type',
                None),
            actor_uuid=obj.get(
                'actor_uuid',
                None),
            role_id=obj.get(
                'role_id',
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
        )
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def type(self):
        """The kind of actor.
        """
        return self._type

    @type.setter
    def type(self, x):
        self._type = x

    @property
    def actor_uuid(self):
        """A pointer to the tool or person based on the associated type.
        """
        return self._actor_uuid

    @actor_uuid.setter
    def actor_uuid(self, x):
        self._actor_uuid = x

    @property
    def role_id(self):
        """For a party, this can optionally be used to specify the role the
        actor was performing.
        """
        return self._role_id

    @role_id.setter
    def role_id(self, x):
        self._role_id = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
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


class Actor(Origin_Actor):
    def __init__(self, **kw):
        super(Actor, self).__init__(**kw)
        self.use_name = 'actor'
