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
    ('english', 'spanish', 'translate.english_spanish');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES
        ('spanish', 'english', 'translate.spanish_english');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES
        ('english', 'french', 'translate.english_french');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='english' and output_language='spanish';""")
    op.execute("""DELETE FROM translation_handler where input_language='spanish' and output_language='english';""")
    op.execute("""DELETE FROM translation_handler where input_language='english' and output_language='french';""")
