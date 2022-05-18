class Plan_Of_Action_And_Milestones:
    """Plan of Action and Milestones (POA&M)

    A plan of action and milestones which identifies initial and residual
risks, deviations, and disposition, such as those required by FedRAMP.

    Attributes:
        uuid (uuid):Uniquely identifies this POA&M. This UUID must
be changed each time the content of the POA&M changes.

        prose (str):Default value holder for raw data in texts

        metadata (str):

        import_ssp (str):

        system_id (str):

        local_definitions (str):

        observation (ARRAY):

        risk (ARRAY):

        poam_item (ARRAY):

        back_matter (str):

    """

    contexts = [
        "oscal-poam",
        "oscal-metadata",
        "oscal-implementation-common",
        "oscal-assessment-common",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "metadata",
        "import_ssp",
        "system_id",
        "local_definitions",
        "observation",
        "risk",
        "poam_item",
        "back_matter",
    ]

    def __init__(
        self,
        uuid,
        metadata,
        poam_item,
        use_name='plan-of-action-and-milestones',
        prose=None,
        import_ssp=None,
        system_id=None,
        local_definitions=None,
        observation=None,
        risk=None,
        back_matter=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._prose = None
        self.prose = \
            prose
        self._metadata = None
        self.metadata = \
            metadata
        self._import_ssp = None
        self.import_ssp = \
            import_ssp
        self._system_id = None
        self.system_id = \
            system_id
        self._local_definitions = None
        self.local_definitions = \
            local_definitions
        self._observation = None
        self.observation = \
            observation
        self._risk = None
        self.risk = \
            risk
        self._poam_item = None
        self.poam_item = \
            poam_item
        self._back_matter = None
        self.back_matter = \
            back_matter
        self.use_name = use_name
        if observation is None:
            self.observation = []
        if risk is None:
            self.risk = []
        if poam_item is None:
            self.poam_item = []

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
            metadata=obj.get(
                'metadata',
                None),
            import_ssp=obj.get(
                'import_ssp',
                None),
            system_id=obj.get(
                'system_id',
                None),
            local_definitions=obj.get(
                'local_definitions',
                None),
            observation=obj.get(
                'observation',
                None),
            risk=obj.get(
                'risk',
                None),
            poam_item=obj.get(
                'poam_item',
                None),
            back_matter=obj.get(
                'back_matter',
                None),
        )
        newcls.observation = \
            obj.get('observations')
        newcls.risk = \
            obj.get('risks')
        newcls.poam_item = \
            obj.get('poam_items')
        return newcls

    @property
    def uuid(self):
        """Uniquely identifies this POA&M. This UUID must be changed each time
        the content of the POA&M changes.
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
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, x):
        self._metadata = x

    @property
    def import_ssp(self):
        return self._import_ssp

    @import_ssp.setter
    def import_ssp(self, x):
        self._import_ssp = x

    @property
    def system_id(self):
        return self._system_id

    @system_id.setter
    def system_id(self, x):
        self._system_id = x

    @property
    def local_definitions(self):
        return self._local_definitions

    @local_definitions.setter
    def local_definitions(self, x):
        self._local_definitions = x

    @property
    def back_matter(self):
        return self._back_matter

    @back_matter.setter
    def back_matter(self, x):
        self._back_matter = x

    @property
    def observation(self):
        return self._observation

    @observation.setter
    def observation(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._observation):
            self._observation = []
        if bool(x):
            if x != self._observation:
                self._observation += list(x)

    @property
    def observations(self):
        return self._observation

    @observations.setter
    def observations(self, x):
        self.observation(x)

    @property
    def risk(self):
        return self._risk

    @risk.setter
    def risk(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._risk):
            self._risk = []
        if bool(x):
            if x != self._risk:
                self._risk += list(x)

    @property
    def risks(self):
        return self._risk

    @risks.setter
    def risks(self, x):
        self.risk(x)

    @property
    def poam_item(self):
        return self._poam_item

    @poam_item.setter
    def poam_item(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._poam_item):
            self._poam_item = []
        if bool(x):
            if x != self._poam_item:
                self._poam_item += list(x)

    @property
    def poam_items(self):
        return self._poam_item

    @poam_items.setter
    def poam_items(self, x):
        self.poam_item(x)
