from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]


def load_dataset(csv_path: str) -> pd.DataFrame:
    caminho = ROOT / "data" / "raw" / csv_path

    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    df = pd.read_csv(caminho, encoding="latin1")

    return df


# if __name__ == "__main__":
#     # Exemplo de uso
#     df = load_dataset("SMSSpamCollection.csv")
#     print(df.head())
