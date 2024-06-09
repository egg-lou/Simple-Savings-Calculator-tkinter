from .base_entry import BaseEntry


class PercentageEntry(BaseEntry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.insert(0, 'Enter Percentage')
