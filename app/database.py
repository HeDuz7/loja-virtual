import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Configuração das chaves
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
service_key: str = os.environ.get("SUPABASE_SERVICE_KEY")

if not url or not key:
    raise ValueError("Verifique as chaves no .env")

# Clientes exportados
supabase: Client = create_client(url, key)
supabase_admin: Client = create_client(url, service_key)