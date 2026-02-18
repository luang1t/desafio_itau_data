from src.gerador_fake import criar_cliente, gerar_dados_csv
from src.etl import run_etl
from src.analise import main as gerar_dashboard

def pipeline_completo():
    print("Iniciando")

    print("\n1/3 - Gerando dados fictícios...")
    gerar_dados_csv(5000)

    print("\n2/3 - Atualizando Banco de Dados...")
    run_etl()

    print("\n3/3 - Gerando Dashboard...")
    gerar_dashboard()

    print("\nFINALIZADO")

if __name__ == "__main__":
    pipeline_completo()
    