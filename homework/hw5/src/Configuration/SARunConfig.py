class SARunConfig:

    runId: str
    initTemp: float
    freezeThreshold: float
    coolRate: float
    equilibriumLen: float

    def __init__(self, runConfig: {}):
        self.runId = runConfig['runId']
        self.initTemp = runConfig['initTemp']
        self.freezeThreshold = runConfig['freezeThreshold']
        self.coolRate = runConfig['coolRate']
        self.equilibriumLen = runConfig['equilibriumLen']
