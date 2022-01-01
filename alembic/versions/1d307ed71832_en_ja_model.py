"""en_ja model

Revision ID: 1d307ed71832
Revises: da213e078ad2
Create Date: 2022-01-02 02:46:35.835069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d307ed71832'
down_revision = 'da213e078ad2'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'ja', 'translate.en_ja');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='ja';""")
