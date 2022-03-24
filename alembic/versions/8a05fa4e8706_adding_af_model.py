"""adding af model

Revision ID: 8a05fa4e8706
Revises: 22f926ffed04
Create Date: 2022-03-25 00:11:28.563061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a05fa4e8706'
down_revision = '22f926ffed04'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'af', 'translate.en_af');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='af';""")
