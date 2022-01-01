"""ja_en model

Revision ID: da213e078ad2
Revises: ad48229638bf
Create Date: 2022-01-02 02:46:29.117794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da213e078ad2'
down_revision = 'ad48229638bf'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('ja', 'en', 'translate.ja_en');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='ja' and output_language='en';""")
