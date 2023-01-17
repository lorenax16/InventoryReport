import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith(".csv"):
            with open(path, "r") as file:
                return list(csv.DictReader(file))
        raise ValueError("Arquivo inválido")
