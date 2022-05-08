"""adding zh model

Revision ID: f974588a7334
Revises: 0f32c1676842
Create Date: 2022-05-09 03:00:05.134992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f974588a7334'
down_revision = '0f32c1676842'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'zh', 'translate.en_zh');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('zh', 'en', 'translate.zh_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('zh', '這是一個測試。');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='zh';""")
    op.execute("""DELETE FROM translation_handler where input_language='zh' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='zh';""")
