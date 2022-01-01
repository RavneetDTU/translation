"""de_en model

Revision ID: 88c8c9ee64d9
Revises: 6bff030edae3
Create Date: 2022-01-02 04:11:27.935960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88c8c9ee64d9'
down_revision = '6bff030edae3'
branch_labels = None
depends_on = None

def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('de', 'en', 'translate.de_en');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='de' and output_language='en';""")
