from supabase import create_client, Client
import os

# Supabase credentials
SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_KEY"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_user(user_id: int, username: str):
    data = {"user_id": user_id, "username": username}
    response = supabase.table("users").insert(data).execute()
    print("User saved:", response)
