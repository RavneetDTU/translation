"""pt_en model

Revision ID: 6874eca39ae3
Revises: 83dc9f680e61
Create Date: 2022-01-02 03:25:55.285807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6874eca39ae3'
down_revision = '83dc9f680e61'
branch_labels = None
depends_on = None

def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('pt', 'en', 'translate.pt_en');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='pt' and output_language='en';""")
