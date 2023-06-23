from api import create_app
from flask.cli import FlaskGroup
from api.extensions.extensions import create_all_tables

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command("create_db")
def create_db():
    """Create the database and all the tables."""
    create_all_tables()

if __name__ == "__main__":
    cli()