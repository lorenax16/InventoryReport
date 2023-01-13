from collections import Counter
from datetime import date


class SimpleReport:
    @classmethod
    def generate(cls, data):
        # empresa com mais produtos
        lista_empresas = [item["nome_da_empresa"] for item in data]
        contador_de_empresa = Counter(lista_empresas)
        produto = contador_de_empresa.most_common(1)[0][0]

        # fabricacao mais antiga
        fabricado_data = [item["data_de_fabricacao"] for item in data]
        fabricacao_mais_velha = min(fabricado_data)

        # validade mais proxima
        hoje = date.today()
        validade = [item["data_de_validade"] for item in data]
        validade_proxima_expirar = []

        for data in validade:
            if date.fromisoformat(data) > hoje:
                validade_proxima_expirar.append(data)
            validade_mais_proxima = min(validade_proxima_expirar)

        return (
            f"Data de fabricação mais antiga: {fabricacao_mais_velha}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com mais produtos: {produto}"
        )
