from _typeshed import Incomplete

class OrganizationLinks:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        _self: Incomplete | None = None,
        members: Incomplete | None = None,
        owners: Incomplete | None = None,
        labels: Incomplete | None = None,
        secrets: Incomplete | None = None,
        buckets: Incomplete | None = None,
        tasks: Incomplete | None = None,
        dashboards: Incomplete | None = None,
    ) -> None: ...
    @property
    def members(self): ...
    @members.setter
    def members(self, members) -> None: ...
    @property
    def owners(self): ...
    @owners.setter
    def owners(self, owners) -> None: ...
    @property
    def labels(self): ...
    @labels.setter
    def labels(self, labels) -> None: ...
    @property
    def secrets(self): ...
    @secrets.setter
    def secrets(self, secrets) -> None: ...
    @property
    def buckets(self): ...
    @buckets.setter
    def buckets(self, buckets) -> None: ...
    @property
    def tasks(self): ...
    @tasks.setter
    def tasks(self, tasks) -> None: ...
    @property
    def dashboards(self): ...
    @dashboards.setter
    def dashboards(self, dashboards) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
