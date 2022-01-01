"""en_id model

Revision ID: b2d880a03256
Revises: 05820f31277d
Create Date: 2022-01-02 01:45:21.623270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2d880a03256'
down_revision = '05820f31277d'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""INSERT INTO translation_handler (input_language, output_language, handler) VALUES ('en', 'id', 'translate.en_id');""")


def downgrade():
    op.execute("""DELETE FROM translation_handler where input_language='en' and output_language='id';""")
