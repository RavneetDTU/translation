"""en_zu model

Revision ID: 9536bd91c599
Revises: d9f529edde7f
Create Date: 2022-01-02 01:32:23.746776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9536bd91c599'
down_revision = 'd9f529edde7f'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'zu', 'translate.en_zu');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='zu';""")
