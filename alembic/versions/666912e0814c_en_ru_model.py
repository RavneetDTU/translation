"""en_ru model

Revision ID: 666912e0814c
Revises: 1d307ed71832
Create Date: 2022-01-02 03:02:21.210108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '666912e0814c'
down_revision = '1d307ed71832'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'ru', 'translate.en_ru');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='ru';""")
