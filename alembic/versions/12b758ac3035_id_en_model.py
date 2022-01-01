"""id_en model

Revision ID: 12b758ac3035
Revises: b2d880a03256
Create Date: 2022-01-02 01:45:34.350895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12b758ac3035'
down_revision = 'b2d880a03256'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('id', 'en', 'translate.id_en');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='id' and output_language='en';""")
