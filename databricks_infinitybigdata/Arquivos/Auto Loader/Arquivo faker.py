import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

def generate_clients_data(start_id, num_rows=1000):
    data = {
        "ID": np.arange(start_id, start_id + num_rows),
        "Nome": [fake.name() for _ in range(num_rows)],
        "Email": [fake.email() for _ in range(num_rows)],
        "Telefone": [fake.phone_number() for _ in range(num_rows)],
        "Endereco": [fake.address() for _ in range(num_rows)]
    }
    return pd.DataFrame(data)

clientes1_df = generate_clients_data(1, 1000)
clientes2_df = generate_clients_data(1001, 1000)
clientes3_df = generate_clients_data(2001, 1000)

clientes1_df.to_parquet("clientes1.parquet", index=False)
clientes2_df.to_parquet("clientes2.parquet", index=False)
clientes3_df.to_parquet("clientes3.parquet", index=False)

print("Arquivos Parquet gerados com sucesso!")

