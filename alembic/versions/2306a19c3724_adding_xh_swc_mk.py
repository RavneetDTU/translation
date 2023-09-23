"""Adding xh swc mk

Revision ID: 2306a19c3724
Revises: 0fae7aef8f56
Create Date: 2023-09-24 03:40:30.166809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2306a19c3724'
down_revision = '0fae7aef8f56'
branch_labels = None
depends_on = None


def upgrade():
    # For xh:
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'xh', 'translate.en_xh');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('xh', 'en', 'translate.xh_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('xh', 'Olu luvavanyo.');""")
    # For swc:
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'swc', 'translate.en_swc');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('swc', 'en', 'translate.swc_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('swc', 'Huu ni mtihani.');""")
    # For mk:
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'mk', 'translate.en_mk');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('mk', 'en', 'translate.mk_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('mk', 'Ова е тест.');""")


def downgrade():
    # For xh:
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='xh';""")
    op.execute("""DELETE FROM translation_handler where input_language='xh' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='xh';""")
    # For swc:
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='swc';""")
    op.execute("""DELETE FROM translation_handler where input_language='swc' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='swc';""")
    # For mk:
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='mk';""")
    op.execute("""DELETE FROM translation_handler where input_language='mk' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='mk';""")

