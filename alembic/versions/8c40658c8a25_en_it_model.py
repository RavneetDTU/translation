"""en_it model

Revision ID: 8c40658c8a25
Revises: c84928445205
Create Date: 2022-01-02 02:37:00.434135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c40658c8a25'
down_revision = 'c84928445205'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'it', 'translate.en_it');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='it';""")
