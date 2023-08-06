"""Adding czech-cs, danish-da, hebrew-ha, polish-pl, swedish-sv, thai-th

Revision ID: 4c346a2ce1fd
Revises: c26b3ea6d99c
Create Date: 2023-08-06 11:02:11.429361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c346a2ce1fd'
down_revision = 'c26b3ea6d99c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'cs', 'translate.en_cs');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('cs', 'en', 'translate.cs_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('cs', 'Això és un test.');""")

    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'da', 'translate.en_da');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('da', 'en', 'translate.da_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('da', 'dette er en test');""")

    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'ha', 'translate.en_ha');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('ha', 'en', 'translate.ha_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('ha', 'זה מבחן');""")

    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'pl', 'translate.en_pl');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('pl', 'en', 'translate.pl_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('pl', 'to jest test');""")

    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'sv', 'translate.en_sv');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('sv', 'en', 'translate.sv_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('sv', 'detta är ett prov');""")

    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'th', 'translate.en_th');""")
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('th', 'en', 'translate.th_en');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('th', 'นี่คือการทดสอบ');""")

def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='cs';""")
    op.execute("""DELETE FROM translation_handler where input_language='cs' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='cs';""")

    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='da';""")
    op.execute("""DELETE FROM translation_handler where input_language='da' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='da';""")

    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='ha';""")
    op.execute("""DELETE FROM translation_handler where input_language='ha' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='ha';""")

    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='pl';""")
    op.execute("""DELETE FROM translation_handler where input_language='pl' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='pl';""")

    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='sv';""")
    op.execute("""DELETE FROM translation_handler where input_language='sv' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='sv';""")

    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='th';""")
    op.execute("""DELETE FROM translation_handler where input_language='th' and output_language='en';""")
    op.execute("""DELETE FROM language_helper where language='th';""")