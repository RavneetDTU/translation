"""en_pt model

Revision ID: 6bff030edae3
Revises: 6874eca39ae3
Create Date: 2022-01-02 03:26:03.745263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bff030edae3'
down_revision = '6874eca39ae3'
branch_labels = None
depends_on = None

def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'pt', 'translate.en_pt');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='pt';""")
