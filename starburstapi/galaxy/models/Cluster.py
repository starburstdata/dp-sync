from dataclasses import dataclass
from typing import List


@dataclass
class Cluster:
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