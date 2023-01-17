import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith("xml"):
            with open(path) as file:
                return xmltodict.parse(file.read())["dataset"]["record"]
        raise ValueError("Arquivo inválido")
