class Security_Impact_Level:
    """Security Impact Level

    The overall level of expected impact resulting from unauthorized
disclosure, modification, or loss of access to information.

    Attributes:
        prose (str):Default value holder for raw data in texts

        security_objective_confidentiality (string):A target-level
of confidentiality for the system, based on the sensitivity
of information within the system.

        security_objective_integrity (string):A target-level of
integrity for the system, based on the sensitivity of
information within the system.

        security_objective_availability (string):A target-level of
availability for the system, based on the sensitivity of
information within the system.

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
        "security_objective_confidentiality",
        "security_objective_integrity",
        "security_objective_availability",
    ]

    def __init__(
        self,
        security_objective_confidentiality,
        security_objective_integrity,
        security_objective_availability,
        use_name='security-impact-level',
        prose=None,
    ):
        self._prose = None
        self.prose = \
            prose
        self._security_objective_confidentiality = None
        self.security_objective_confidentiality = \
            security_objective_confidentiality
        self._security_objective_integrity = None
        self.security_objective_integrity = \
            security_objective_integrity
        self._security_objective_availability = None
        self.security_objective_availability = \
            security_objective_availability
        self.use_name = use_name

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            prose=obj.get(
                'prose',
                None),
            security_objective_confidentiality=obj.get(
                'security_objective_confidentiality',
                None),
            security_objective_integrity=obj.get(
                'security_objective_integrity',
                None),
            security_objective_availability=obj.get(
                'security_objective_availability',
                None),
        )
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
    def security_objective_confidentiality(self):
        """A target-level of confidentiality for the system, based on the
        sensitivity of information within the system.
        """
        return self._security_objective_confidentiality

    @security_objective_confidentiality.setter
    def security_objective_confidentiality(self, x):
        self._security_objective_confidentiality = x

    @property
    def security_objective_integrity(self):
        """A target-level of integrity for the system, based on the sensitivity
        of information within the system.
        """
        return self._security_objective_integrity

    @security_objective_integrity.setter
    def security_objective_integrity(self, x):
        self._security_objective_integrity = x

    @property
    def security_objective_availability(self):
        """A target-level of availability for the system, based on the
        sensitivity of information within the system.
        """
        return self._security_objective_availability

    @security_objective_availability.setter
    def security_objective_availability(self, x):
        self._security_objective_availability = x
