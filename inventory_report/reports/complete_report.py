from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        relatorio_simples = super().generate(data)

        lista_empresas = [item["nome_da_empresa"] for item in data]
        contador_de_empresa = Counter(lista_empresas).items()
        relatorio_completo = ""

        for empresa, qtd_produto in contador_de_empresa:
            relatorio_completo += f"- {empresa}: {qtd_produto}\n"

        return (
            f"{relatorio_simples}\n"
            f"Produtos estocados por empresa:\n"
            f"{relatorio_completo}"
        )
