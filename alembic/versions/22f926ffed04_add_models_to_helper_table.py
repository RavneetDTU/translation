"""add models to helper_table

Revision ID: 22f926ffed04
Revises: 7914e372802d
Create Date: 2022-01-04 17:32:00.565424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22f926ffed04'
down_revision = '7914e372802d'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('en', 'This is a test');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('fr', 'これはテストです。');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('es', 'C'est un test.');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('pt', 'Isto é um teste.');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('de', 'Das ist ein Test.');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('ru', 'Это тест.');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('zu', 'Lokhu ukuhlolwa.');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('nl', 'Dit is een test.');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('it', 'Questo è un test.');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('id', 'Ini adalah sebuah ujian.');""")
    op.execute("""INSERT INTO language_helper (language, sample_text) VALUES ('ja', 'これはテストです。');""")


def downgrade():
    op.execute("""DELETE FROM language_helper where language='en';""")
    op.execute("""DELETE FROM language_helper where language='fr';""")
    op.execute("""DELETE FROM language_helper where language='es';""")
    op.execute("""DELETE FROM language_helper where language='pt';""")
    op.execute("""DELETE FROM language_helper where language='de';""")
    op.execute("""DELETE FROM language_helper where language='ru';""")
    op.execute("""DELETE FROM language_helper where language='zu';""")
    op.execute("""DELETE FROM language_helper where language='nl';""")
    op.execute("""DELETE FROM language_helper where language='it';""")
    op.execute("""DELETE FROM language_helper where language='id';""")
    op.execute("""DELETE FROM language_helper where language='ja';""")
