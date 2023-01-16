import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path, tipo):

        with open(path) as file:
            relatorio_csv = list(csv.DictReader(file))
        if tipo == "simples":
            return SimpleReport.generate(relatorio_csv)
        elif tipo == "completo":
            return CompleteReport.generate(relatorio_csv)
        else:
            raise ValueError("Tipo inválido")
