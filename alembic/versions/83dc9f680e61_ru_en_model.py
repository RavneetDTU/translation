"""ru_en model

Revision ID: 83dc9f680e61
Revises: 666912e0814c
Create Date: 2022-01-02 03:02:32.027462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83dc9f680e61'
down_revision = '666912e0814c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('ru', 'en', 'translate.ru_en');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='ru' and output_language='en';""")
