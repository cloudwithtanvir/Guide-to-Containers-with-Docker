from alembic import op
import sqlalchemy as sa


# Define the table schema
def upgrade():
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, index=True),
        sa.Column('author', sa.String, index=True),
        sa.Column('pages', sa.Integer)
    )


def downgrade():
    op.drop_table('books')
