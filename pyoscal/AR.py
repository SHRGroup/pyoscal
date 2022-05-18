from .core.oscal_metadata import (
    Metadata, Last_Modified, Version, Oscal_Version,
    Title as metaTitle, Uuid
)

from .core.oscal_assessment_common import (
    Href, Reviewed_Controls, Control_Selection, Select_Control_By_Id,
    Title, Start, Description
)

from .core.oscal_ar import (
    Assessment_Results, Result, Import_Ap, Finding
)
from .OSCAL import Oscal
from .common import getToday, createUUID


class AR(Oscal):

    def __init__(
        self,
        title,
        version=getToday(fmt='day'),
        oscal_version=getToday(),
        last_modified=getToday(),
        uuid=createUUID(),
        plan='some_plan_href'
    ):

        metadata = Metadata.Metadata(
            title=metaTitle.Title(prose=title),
            last_modified=Last_Modified.Last_Modified(prose=last_modified),
            version=Version.Version(prose=version),
            oscal_version=Oscal_Version.Oscal_Version(prose=oscal_version),
        )

        self.oscal = Assessment_Results.Assessment_Results(
                uuid=Uuid.Uuid(prose=uuid),
                metadata=metadata,
                import_ap=Import_Ap.Import_Ap(href=Href.Href(prose=plan)),
                result=None,
        )

    def add_result(
        self,
        uuid=createUUID(),
        title="Result",
        description="",
        start=getToday(),
        controls=[],
        finding=(None, None)
    ):

        controls = [
            Reviewed_Controls.Reviewed_Controls(
                control_selection=Control_Selection.Control_Selection(
                    include_all=None,
                    include_control=Select_Control_By_Id.Include_Control(
                        control_id=c)
                )
            )
            for c in controls
        ]

        result = Result.Result(
            uuid=Uuid.Uuid(prose=uuid),
            title=Title.Title(prose=title),
            start=Start.Start(prose=start),
            reviewed_controls=controls,
            description=Description.Description(prose=description),
            finding=Finding.Finding(
                uuid=Uuid.Uuid(prose=createUUID()),
                title=Title.Title(prose=finding[0]),
                description=Description.Description(prose=finding[1])
            )
        )
        self.oscal.result = result
