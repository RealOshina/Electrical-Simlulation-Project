class Transistor:
    def __init__(self, base=0, collector=1, emitter=2, hfe=100, vbe=0.7):
        self.base = base
        self.collector = collector
        self.emitter = emitter
        self.hfe = hfe
        self.vbe = vbe