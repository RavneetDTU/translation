"""zu_en model

Revision ID: 05820f31277d
Revises: 9536bd91c599
Create Date: 2022-01-02 01:34:31.811207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05820f31277d'
down_revision = '9536bd91c599'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('zu', 'en', 'translate.en_es');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='zu' and output_language='en';""")
