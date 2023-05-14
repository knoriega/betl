import pandas as pd

def iris_melter(iris: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(
        iris,
        id_vars=["species"],
        value_vars=[col for col in iris.columns if col != "species"]
    )
