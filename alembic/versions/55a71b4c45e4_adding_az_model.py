"""adding az model

Revision ID: 55a71b4c45e4
Revises: 2ae691d00872
Create Date: 2022-08-09 07:28:20.064638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55a71b4c45e4'
down_revision = '2ae691d00872'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'az', 'translate.en_az');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('az', 'en', 'translate.az_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('az', 'Bu testdir.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='az';""")
    op.execute("""DELETE FROM translation_handler where input_language='az' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='az';""")
