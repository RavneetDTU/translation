"""Adding Bulgarian model

Revision ID: 0fae7aef8f56
Revises: 4c346a2ce1fd
Create Date: 2023-09-24 03:26:21.494151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fae7aef8f56'
down_revision = '4c346a2ce1fd'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'bg', 'translate.en_bg');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('bg', 'en', 'translate.bg_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('bg', 'Това е тест.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='bg';""")
    op.execute("""DELETE FROM translation_handler where input_language='bg' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='bg';""")
