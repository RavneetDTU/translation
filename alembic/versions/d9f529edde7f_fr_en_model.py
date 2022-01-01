"""fr_en_model

Revision ID: d9f529edde7f
Revises: 2eef5020a22f
Create Date: 2022-01-01 14:31:21.788185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9f529edde7f'
down_revision = '2eef5020a22f'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('fr', 'en', 'translate.fr_en');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='fr' and output_language='en';""")
