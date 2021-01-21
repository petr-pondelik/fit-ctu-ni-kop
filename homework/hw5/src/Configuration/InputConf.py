class InputConf:

    path: str
    filenameFragment: str
    format: str
    start: int
    end: int

    def __init__(self, conf: {}):
        self.path = conf['path']
        self.filenameFragment = conf['filenameFragment']
        self.format = conf['format']
        self.start = conf['start']
        self.end = conf['end']
