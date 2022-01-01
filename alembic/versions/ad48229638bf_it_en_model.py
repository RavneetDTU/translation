"""it_en model

Revision ID: ad48229638bf
Revises: 8c40658c8a25
Create Date: 2022-01-02 02:37:07.764155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad48229638bf'
down_revision = '8c40658c8a25'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('it', 'en', 'translate.it_en');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='it' and output_language='en';""")
