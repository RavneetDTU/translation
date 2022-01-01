"""en_nl model

Revision ID: c84928445205
Revises: b1ffc7e01b92
Create Date: 2022-01-02 02:10:32.823722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c84928445205'
down_revision = 'b1ffc7e01b92'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'nl', 'translate.en_nl');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='nl';""")
