class Party:
    """Party (organization or person)

    A responsible entity which is either a person or an organization.

    Attributes:
        uuid (uuid):A unique identifier that can be used to
reference this defined location elsewhere in an OSCAL
document. A UUID should be consistently used for a given
party across revisions of the document.

        type (string):A category describing the kind of party the
object describes.

        prose (str):Default value holder for raw data in texts

        name (str):The full name of the party. This is typically the
legal name associated with the party.

        short_name (str):A short common name, abbreviation, or
acronym for the party.

        external_id (ARRAY):An identifier for a person or
organization using a designated scheme. e.g. an Open
Researcher and Contributor ID (ORCID)

        oscal_property (ARRAY):

        link (ARRAY):

        email_address (ARRAY):

        telephone_number (ARRAY):

        member_of_organization (ARRAY):Identifies that the party
object is a member of the organization associated with the
provided UUID.

        remarks (str):

        address (ARRAY):

        location_uuid (ARRAY):

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "uuid",
        "type",
    ]
    subcomponents = [
        "prose",
        "name",
        "short_name",
        "external_id",
        "oscal_property",
        "link",
        "email_address",
        "telephone_number",
        "member_of_organization",
        "remarks",
        "address",
        "location_uuid",
    ]

    def __init__(
        self,
        uuid,
        type,
        use_name='party',
        prose=None,
        name=None,
        short_name=None,
        external_id=None,
        oscal_property=None,
        link=None,
        email_address=None,
        telephone_number=None,
        member_of_organization=None,
        remarks=None,
        address=None,
        location_uuid=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._type = None
        self.type = \
            type
        self._prose = None
        self.prose = \
            prose
        self._name = None
        self.name = \
            name
        self._short_name = None
        self.short_name = \
            short_name
        self._external_id = None
        self.external_id = \
            external_id
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._email_address = None
        self.email_address = \
            email_address
        self._telephone_number = None
        self.telephone_number = \
            telephone_number
        self._member_of_organization = None
        self.member_of_organization = \
            member_of_organization
        self._remarks = None
        self.remarks = \
            remarks
        self._address = None
        self.address = \
            address
        self._location_uuid = None
        self.location_uuid = \
            location_uuid
        self.use_name = use_name
        if external_id is None:
            self.external_id = []
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []
        if email_address is None:
            self.email_address = []
        if telephone_number is None:
            self.telephone_number = []
        if member_of_organization is None:
            self.member_of_organization = []
        if address is None:
            self.address = []
        if location_uuid is None:
            self.location_uuid = []

    def __str__(self):

        return str(self.prose)

    @classmethod
    def fromDict(cls, obj):
        newcls = cls(
            uuid=obj.get(
                'uuid',
                None),
            type=obj.get(
                'type',
                None),
            prose=obj.get(
                'prose',
                None),
            name=obj.get(
                'name',
                None),
            short_name=obj.get(
                'short_name',
                None),
            external_id=obj.get(
                'external_id',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            email_address=obj.get(
                'email_address',
                None),
            telephone_number=obj.get(
                'telephone_number',
                None),
            member_of_organization=obj.get(
                'member_of_organization',
                None),
            remarks=obj.get(
                'remarks',
                None),
            address=obj.get(
                'address',
                None),
            location_uuid=obj.get(
                'location_uuid',
                None),
        )
        newcls.external_id = \
            obj.get('external_ids')
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.email_address = \
            obj.get('email_addresses')
        newcls.telephone_number = \
            obj.get('telephone_numbers')
        newcls.member_of_organization = \
            obj.get('member_of_organizations')
        newcls.address = \
            obj.get('addresses')
        newcls.location_uuid = \
            obj.get('location_uuids')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """A unique identifier that can be used to reference this defined
        location elsewhere in an OSCAL document. A UUID should be
        consistently used for a given party across revisions of the
        document.
        """
        return self._uuid

    @uuid.setter
    def uuid(self, x):
        self._uuid = x

    @property
    def type(self):
        """A category describing the kind of party the object describes.
        """
        return self._type

    @type.setter
    def type(self, x):
        self._type = x

    @property
    def prose(self):
        """Default value holder for raw data in texts
        """
        return self._prose

    @prose.setter
    def prose(self, x):
        self._prose = x

    @property
    def name(self):
        """The full name of the party. This is typically the legal name
        associated with the party.
        """
        return self._name

    @name.setter
    def name(self, x):
        self._name = x

    @property
    def short_name(self):
        """A short common name, abbreviation, or acronym for the party.
        """
        return self._short_name

    @short_name.setter
    def short_name(self, x):
        self._short_name = x

    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, x):
        self._remarks = x

    @property
    def external_id(self):
        """An identifier for a person or organization using a designated
        scheme. e.g. an Open Researcher and Contributor ID (ORCID)
        """
        return self._external_id

    @external_id.setter
    def external_id(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._external_id):
            self._external_id = []
        if bool(x):
            if x != self._external_id:
                self._external_id += list(x)

    @property
    def external_ids(self):
        return self._external_id

    @external_ids.setter
    def external_ids(self, x):
        self.external_id(x)

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
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._email_address):
            self._email_address = []
        if bool(x):
            if x != self._email_address:
                self._email_address += list(x)

    @property
    def email_addresses(self):
        return self._email_address

    @email_addresses.setter
    def email_addresses(self, x):
        self.email_address(x)

    @property
    def telephone_number(self):
        return self._telephone_number

    @telephone_number.setter
    def telephone_number(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._telephone_number):
            self._telephone_number = []
        if bool(x):
            if x != self._telephone_number:
                self._telephone_number += list(x)

    @property
    def telephone_numbers(self):
        return self._telephone_number

    @telephone_numbers.setter
    def telephone_numbers(self, x):
        self.telephone_number(x)

    @property
    def member_of_organization(self):
        """Identifies that the party object is a member of the organization
        associated with the provided UUID.
        """
        return self._member_of_organization

    @member_of_organization.setter
    def member_of_organization(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._member_of_organization):
            self._member_of_organization = []
        if bool(x):
            if x != self._member_of_organization:
                self._member_of_organization += list(x)

    @property
    def member_of_organizations(self):
        return self._member_of_organization

    @member_of_organizations.setter
    def member_of_organizations(self, x):
        self.member_of_organization(x)

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._address):
            self._address = []
        if bool(x):
            if x != self._address:
                self._address += list(x)

    @property
    def addresses(self):
        return self._address

    @addresses.setter
    def addresses(self, x):
        self.address(x)

    @property
    def location_uuid(self):
        return self._location_uuid

    @location_uuid.setter
    def location_uuid(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._location_uuid):
            self._location_uuid = []
        if bool(x):
            if x != self._location_uuid:
                self._location_uuid += list(x)

    @property
    def location_uuids(self):
        return self._location_uuid

    @location_uuids.setter
    def location_uuids(self, x):
        self.location_uuid(x)
