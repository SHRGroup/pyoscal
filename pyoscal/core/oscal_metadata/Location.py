class Location:
    """Location

    A location, with associated metadata that can be referenced.

    Attributes:
        uuid (uuid):A unique identifier that can be used to
reference this defined location elsewhere in an OSCAL
document. A UUID should be consistently used for a given
location across revisions of the document.

        prose (str):Default value holder for raw data in texts

        title (markup-line):A name given to the location, which may
be used by a tool for display and navigation.

        address (str):

        email_address (ARRAY):

        telephone_number (ARRAY):

        url (ARRAY):The uniform resource locator (URL) for a web
site or Internet presence associated with the location.

        oscal_property (ARRAY):

        link (ARRAY):

        remarks (str):

    """

    contexts = [
        "oscal-metadata",
    ]
    parameters = [
        "uuid",
    ]
    subcomponents = [
        "prose",
        "title",
        "address",
        "email_address",
        "telephone_number",
        "url",
        "oscal_property",
        "link",
        "remarks",
    ]

    def __init__(
        self,
        uuid,
        address,
        use_name='location',
        prose=None,
        title=None,
        email_address=None,
        telephone_number=None,
        url=None,
        oscal_property=None,
        link=None,
        remarks=None,
    ):
        self._uuid = None
        self.uuid = \
            uuid
        self._prose = None
        self.prose = \
            prose
        self._title = None
        self.title = \
            title
        self._address = None
        self.address = \
            address
        self._email_address = None
        self.email_address = \
            email_address
        self._telephone_number = None
        self.telephone_number = \
            telephone_number
        self._url = None
        self.url = \
            url
        self._oscal_property = None
        self.oscal_property = \
            oscal_property
        self._link = None
        self.link = \
            link
        self._remarks = None
        self.remarks = \
            remarks
        self.use_name = use_name
        if email_address is None:
            self.email_address = []
        if telephone_number is None:
            self.telephone_number = []
        if url is None:
            self.url = []
        if oscal_property is None:
            self.oscal_property = []
        if link is None:
            self.link = []

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
            title=obj.get(
                'title',
                None),
            address=obj.get(
                'address',
                None),
            email_address=obj.get(
                'email_address',
                None),
            telephone_number=obj.get(
                'telephone_number',
                None),
            url=obj.get(
                'url',
                None),
            oscal_property=obj.get(
                'oscal_property',
                None),
            link=obj.get(
                'link',
                None),
            remarks=obj.get(
                'remarks',
                None),
        )
        newcls.email_address = \
            obj.get('email_addresses')
        newcls.telephone_number = \
            obj.get('telephone_numbers')
        newcls.url = \
            obj.get('urls')
        newcls.oscal_property = \
            obj.get('props')
        newcls.link = \
            obj.get('links')
        newcls.oscal_property = \
            obj.get('prop')
        return newcls

    @property
    def uuid(self):
        """A unique identifier that can be used to reference this defined
        location elsewhere in an OSCAL document. A UUID should be
        consistently used for a given location across revisions of the
        document.
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
    def title(self):
        """A name given to the location, which may be used by a tool for
        display and navigation.
        """
        return self._title

    @title.setter
    def title(self, x):
        self._title = x

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, x):
        self._address = x

    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, x):
        self._remarks = x

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
    def url(self):
        """The uniform resource locator (URL) for a web site or Internet
        presence associated with the location.
        """
        return self._url

    @url.setter
    def url(self, x):
        if not isinstance(x, list) and x is not None:
            x = [x]
        if not bool(self._url):
            self._url = []
        if bool(x):
            if x != self._url:
                self._url += list(x)

    @property
    def urls(self):
        return self._url

    @urls.setter
    def urls(self, x):
        self.url(x)

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
