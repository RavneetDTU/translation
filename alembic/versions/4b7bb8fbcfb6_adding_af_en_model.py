"""adding af_en model

Revision ID: 4b7bb8fbcfb6
Revises: 8a05fa4e8706
Create Date: 2022-03-25 00:35:52.890896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b7bb8fbcfb6'
down_revision = '8a05fa4e8706'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('af', 'en', 'translate.af_en');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='af' and output_language='en';""")
