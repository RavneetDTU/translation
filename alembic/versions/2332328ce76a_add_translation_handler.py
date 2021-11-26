"""add translation handler

Revision ID: 2332328ce76a
Revises: 0862346b53e7
Create Date: 2021-11-21 23:42:02.528327

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '2332328ce76a'
down_revision = '0862346b53e7'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES
    ('en', 'es', 'translate.en_es');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES
        ('es', 'en', 'translate.es_en');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES
        ('en', 'fr', 'translate.en_fr');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='es';""")
    op.execute("""DELETE FROM translation_handler where input_language='es' and output_language='en';""")
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='fr';""")
