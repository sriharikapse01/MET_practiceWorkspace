from supabase import create_client, Client

# Replace with your values
SUPABASE_URL = "https://ytsobozpwdwhmwxgivhv.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl0c29ib3pwd2R3aG13eGdpdmh2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA0NTAzMTksImV4cCI6MjA2NjAyNjMxOX0.5o2oRTH5b3y25WVfM0aGO6MBXejgYRaUfZ-MGHWfEF0"

def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)
