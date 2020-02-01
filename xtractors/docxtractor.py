import docx


class DocExtractor(object):

    def __init__(self, docx_filepath):
        self.object = docx.Document(str(docx_filepath))

    def get_plaintext(self):
        lines = [p.text for p in self.object.paragraphs]
        return '\n'.join(lines)
