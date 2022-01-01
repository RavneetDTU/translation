"""en_de model

Revision ID: 7914e372802d
Revises: 88c8c9ee64d9
Create Date: 2022-01-02 04:11:35.658497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7914e372802d'
down_revision = '88c8c9ee64d9'
branch_labels = None
depends_on = None

def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'de', 'translate.en_de');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='de';""")
