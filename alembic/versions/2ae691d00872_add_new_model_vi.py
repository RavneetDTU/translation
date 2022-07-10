"""add new model vi

Revision ID: 2ae691d00872
Revises: 2f10441ef486
Create Date: 2022-07-11 00:53:06.866251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ae691d00872'
down_revision = '2f10441ef486'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'vi', 'translate.en_vi');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('vi', 'en', 'translate.vi_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('vi', 'Đây là một bài kiểm tra.');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='vi';""")
    op.execute("""DELETE FROM translation_handler where input_language='vi' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='vi';""")
