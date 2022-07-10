"""add new model hindi

Revision ID: d52e55cd3829
Revises: f4c711c1f576
Create Date: 2022-07-10 18:17:30.706230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd52e55cd3829'
down_revision = 'f4c711c1f576'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'hi', 'translate.en_hi');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('hi', 'en', 'translate.hi_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('hi', 'यह टेस्ट है।');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='hi';""")
    op.execute("""DELETE FROM translation_handler where input_language='hi' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='hi';""")
