from dataclasses import dataclass
from typing import List
from starburstapi.shared.models import PaginatedJsonDataClass

@dataclass
class Cluster(PaginatedJsonDataClass):
    syncToken: str
    clusterId: str
    name: str
    cloudRegionId: str
    catalogRefs: List[str]
    idleStopMinutes: int
    batchCluster: bool
    warpSpeedCluster: bool
    minWorkers: int
    maxWorkers: int
    clusterState: str
    trinoUri: str