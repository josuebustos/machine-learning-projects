from your_app import create_app
from app.config import DATABASE_URL

app = create_app()
database = Database(DATABASE_URL)


def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_schemas=True,
    )
