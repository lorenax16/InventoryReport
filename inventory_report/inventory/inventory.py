from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def verificar_arquivo(path):
        if path.endswith(".csv"):
            importer_list = CsvImporter.import_data(path)
        elif path.endswith(".json"):
            importer_list = JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            importer_list = XmlImporter.import_data(path)
        return importer_list
        # https://algoritmosempython.com.br/cursos/programacao-python/strings/
        # A string s termina com "mundo"?
        # print(s.endswith("mundo"))

    @staticmethod
    def import_data(path, tipo):

        arquivo = Inventory.verificar_arquivo(path)
        if tipo == "simples":
            return SimpleReport.generate(arquivo)
        elif tipo == "completo":
            return CompleteReport.generate(arquivo)
        else:
            raise ValueError("Tipo inválido")
