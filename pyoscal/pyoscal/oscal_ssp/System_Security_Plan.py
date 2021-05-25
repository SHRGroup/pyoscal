class System_Security_Plan:
    """System Security Plan (SSP)

    A system security plan, such as those described in NIST SP 800-18

    Attributes:
        uuid (uuid):A globally unique identifier for this catalog
instance. This UUID should be changed when this document is
revised.

        prose (str):Default value holder for raw data in texts

        metadata (str):

        import_profile (str):

        system_characteristics (str):

        system_implementation (str):

        control_implementation (str):

        back_matter (str):

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
        "metadata",
        "import_profile",
        "system_characteristics",
        "system_implementation",
        "control_implementation",
        "back_matter",
    ]

    def __init__(
        self,
        uuid,
        metadata,
        import_profile,
        system_characteristics,
        system_implementation,
        control_implementation,
        use_name='system-security-plan',
        prose=None,
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
        self._import_profile = None
        self.import_profile = \
            import_profile
        self._system_characteristics = None
        self.system_characteristics = \
            system_characteristics
        self._system_implementation = None
        self.system_implementation = \
            system_implementation
        self._control_implementation = None
        self.control_implementation = \
            control_implementation
        self._back_matter = None
        self.back_matter = \
            back_matter
        self.use_name = use_name

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
            import_profile=obj.get(
                'import_profile',
                None),
            system_characteristics=obj.get(
                'system_characteristics',
                None),
            system_implementation=obj.get(
                'system_implementation',
                None),
            control_implementation=obj.get(
                'control_implementation',
                None),
            back_matter=obj.get(
                'back_matter',
                None),
        )
        return newcls

    @property
    def uuid(self):
        """A globally unique identifier for this catalog instance. This UUID
        should be changed when this document is revised.
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
    def import_profile(self):
        return self._import_profile

    @import_profile.setter
    def import_profile(self, x):
        self._import_profile = x

    @property
    def system_characteristics(self):
        return self._system_characteristics

    @system_characteristics.setter
    def system_characteristics(self, x):
        self._system_characteristics = x

    @property
    def system_implementation(self):
        return self._system_implementation

    @system_implementation.setter
    def system_implementation(self, x):
        self._system_implementation = x

    @property
    def control_implementation(self):
        return self._control_implementation

    @control_implementation.setter
    def control_implementation(self, x):
        self._control_implementation = x

    @property
    def back_matter(self):
        return self._back_matter

    @back_matter.setter
    def back_matter(self, x):
        self._back_matter = x
