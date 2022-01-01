"""nl_en model

Revision ID: b1ffc7e01b92
Revises: 12b758ac3035
Create Date: 2022-01-02 02:10:21.958841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1ffc7e01b92'
down_revision = '12b758ac3035'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('nl', 'en', 'translate.nl_en');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='nl' and output_language='en';""")
