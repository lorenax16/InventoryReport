from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        relatorio = super().generate(data)
        empresas_lista = [item["nome_da_empresa"] for item in data]
        qtd_produtos_da_empresa = Counter(empresas_lista).items()
        relatorio += "\nProdutos estocados por empresa:\n"

        for empresa, qtd_produto in qtd_produtos_da_empresa:
            relatorio += f"- {empresa} : {qtd_produto}"

        return relatorio
