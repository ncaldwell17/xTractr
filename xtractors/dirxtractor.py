import glob


class DirExtractor(object):

    def __init__(self, directory_path):
        self.dir = directory_path

    def retrieve_extension_pattern(self, extension):
        retrieved = glob.glob(self.dir+"/*"+extension)
        return retrieved

