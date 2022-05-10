"""adding korean model

Revision ID: f4c711c1f576
Revises: f974588a7334
Create Date: 2022-05-10 22:34:58.140690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4c711c1f576'
down_revision = 'f974588a7334'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'ko', 'translate.en_ko');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('ko', 'en', 'translate.ko_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('ko', '이것은 테스트입니다.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='ko';""")
    op.execute("""DELETE FROM translation_handler where input_language='ko' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='ko';""")
