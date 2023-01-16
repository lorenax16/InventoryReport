import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def verificar_arquivo(path):
        if path.endswith(".csv"):
            with open(path) as file:
                return list(csv.DictReader(file))
        elif path.endswith(".json"):
            with open(path, "r") as file:
                return json.load(file)
        else:
            with open(path) as file:
                return xmltodict.parse(file.read())["dataset"]["record"]
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
