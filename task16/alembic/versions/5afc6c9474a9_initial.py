"""Initial

Revision ID: 5afc6c9474a9
Revises: 
Create Date: 2025-06-09 23:10:33.990854

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '5afc6c9474a9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('main_categorys_name_fb3ce484_like'), table_name='main_categorys')
    op.drop_index(op.f('main_categorys_slug_a2dfb325_like'), table_name='main_categorys')
    op.drop_table('main_categorys')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    op.drop_table('main_contactmessage')
    op.drop_index(op.f('django_session_expire_date_a5c62663'), table_name='django_session')
    op.drop_index(op.f('django_session_session_key_c0390e0f_like'), table_name='django_session')
    op.drop_table('django_session')
    op.drop_table('django_migrations')
    op.drop_index(op.f('auth_user_user_permissions_permission_id_1fbb5f2c'), table_name='auth_user_user_permissions')
    op.drop_index(op.f('auth_user_user_permissions_user_id_a95ead1b'), table_name='auth_user_user_permissions')
    op.drop_table('auth_user_user_permissions')
    op.drop_index(op.f('auth_group_permissions_group_id_b120cbf9'), table_name='auth_group_permissions')
    op.drop_index(op.f('auth_group_permissions_permission_id_84c5c92e'), table_name='auth_group_permissions')
    op.drop_table('auth_group_permissions')
    op.drop_index(op.f('main_product_category_id_c0d90f41'), table_name='main_product')
    op.drop_index(op.f('main_product_slug_85058272_like'), table_name='main_product')
    op.drop_table('main_product')
    op.drop_index(op.f('main_productreview_product_id_b0d42925'), table_name='main_productreview')
    op.drop_index(op.f('main_productreview_user_id_bdd4771a'), table_name='main_productreview')
    op.drop_table('main_productreview')
    op.drop_index(op.f('main_cart_user_id_53cf8b47'), table_name='main_cart')
    op.drop_table('main_cart')
    op.drop_index(op.f('main_subscriber_email_f306f4bd_like'), table_name='main_subscriber')
    op.drop_table('main_subscriber')
    op.drop_index(op.f('django_admin_log_content_type_id_c4bce8eb'), table_name='django_admin_log')
    op.drop_index(op.f('django_admin_log_user_id_c564eba6'), table_name='django_admin_log')
    op.drop_table('django_admin_log')
    op.drop_table('main_video')
    op.drop_index(op.f('main_category_parent_id_212af219'), table_name='main_category')
    op.drop_index(op.f('main_category_slug_7ae6758d_like'), table_name='main_category')
    op.drop_table('main_category')
    op.drop_index(op.f('main_cartitem_cart_id_8357cf81'), table_name='main_cartitem')
    op.drop_index(op.f('main_cartitem_product_id_777783fc'), table_name='main_cartitem')
    op.drop_table('main_cartitem')
    op.drop_index(op.f('auth_user_groups_group_id_97559544'), table_name='auth_user_groups')
    op.drop_index(op.f('auth_user_groups_user_id_6a12ed8b'), table_name='auth_user_groups')
    op.drop_table('auth_user_groups')
    op.drop_index(op.f('auth_user_username_6821ab7c_like'), table_name='auth_user')
    op.drop_table('auth_user')
    op.drop_index(op.f('auth_permission_content_type_id_2f476e4b'), table_name='auth_permission')
    op.drop_table('auth_permission')
    op.drop_index(op.f('main_products_category_id_f63e0baa'), table_name='main_products')
    op.drop_table('main_products')
    op.drop_index(op.f('auth_group_name_a6ea08ec_like'), table_name='auth_group')
    op.drop_table('auth_group')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    op.drop_table('main_banner')
    op.drop_index(op.f('main_productfeature_product_id_a4b291e6'), table_name='main_productfeature')
    op.drop_table('main_productfeature')
    op.drop_index(op.f('main_productimage_product_id_7c7e66ae'), table_name='main_productimage')
    op.drop_table('main_productimage')
    op.drop_table('django_content_type')
    op.add_column('note', sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('note', sa.Column('content', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.drop_column('note', 'created_at')
    op.drop_column('note', 'text')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note', sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('note', sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('note', 'content')
    op.drop_column('note', 'title')
    op.create_table('django_content_type',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app_label', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('model', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_content_type_pkey'),
    sa.UniqueConstraint('app_label', 'model', name='django_content_type_app_label_model_76bd3d3b_uniq', postgresql_include=[], postgresql_nulls_not_distinct=False),
    postgresql_ignore_search_path=False
    )
    op.create_table('main_productimage',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('image', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('order', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('product_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('caption', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['main_product.id'], name=op.f('main_productimage_product_id_7c7e66ae_fk_main_product_id'), initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('main_productimage_pkey'))
    )
    op.create_index(op.f('main_productimage_product_id_7c7e66ae'), 'main_productimage', ['product_id'], unique=False)
    op.create_table('main_productfeature',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('text', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('order', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('product_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.CheckConstraint('"order" >= 0', name=op.f('main_productfeature_order_check')),
    sa.ForeignKeyConstraint(['product_id'], ['main_product.id'], name=op.f('main_productfeature_product_id_a4b291e6_fk_main_product_id'), initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('main_productfeature_pkey'))
    )
    op.create_index(op.f('main_productfeature_product_id_a4b291e6'), 'main_productfeature', ['product_id'], unique=False)
    op.create_table('main_banner',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('image', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('link', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('order', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('main_banner_pkey'))
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('users_pkey'))
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('auth_group',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_group_pkey'),
    sa.UniqueConstraint('name', name='auth_group_name_key', postgresql_include=[], postgresql_nulls_not_distinct=False),
    postgresql_ignore_search_path=False
    )
    op.create_index(op.f('auth_group_name_a6ea08ec_like'), 'auth_group', ['name'], unique=False)
    op.create_table('main_products',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('image', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('price', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('category_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('sku', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['main_categorys.id'], name='main_products_category_id_f63e0baa_fk_main_categorys_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='main_products_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index(op.f('main_products_category_id_f63e0baa'), 'main_products', ['category_id'], unique=False)
    op.create_table('auth_permission',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codename', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='auth_permission_content_type_id_2f476e4b_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_permission_pkey'),
    sa.UniqueConstraint('content_type_id', 'codename', name='auth_permission_content_type_id_codename_01ab375a_uniq', postgresql_include=[], postgresql_nulls_not_distinct=False),
    postgresql_ignore_search_path=False
    )
    op.create_index(op.f('auth_permission_content_type_id_2f476e4b'), 'auth_permission', ['content_type_id'], unique=False)
    op.create_table('auth_user',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('last_login', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=254), autoincrement=False, nullable=False),
    sa.Column('is_staff', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('date_joined', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_user_pkey'),
    sa.UniqueConstraint('username', name='auth_user_username_key', postgresql_include=[], postgresql_nulls_not_distinct=False),
    postgresql_ignore_search_path=False
    )
    op.create_index(op.f('auth_user_username_6821ab7c_like'), 'auth_user', ['username'], unique=False)
    op.create_table('auth_user_groups',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name=op.f('auth_user_groups_group_id_97559544_fk_auth_group_id'), initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name=op.f('auth_user_groups_user_id_6a12ed8b_fk_auth_user_id'), initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('auth_user_groups_pkey')),
    sa.UniqueConstraint('user_id', 'group_id', name=op.f('auth_user_groups_user_id_group_id_94350c0c_uniq'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_index(op.f('auth_user_groups_user_id_6a12ed8b'), 'auth_user_groups', ['user_id'], unique=False)
    op.create_index(op.f('auth_user_groups_group_id_97559544'), 'auth_user_groups', ['group_id'], unique=False)
    op.create_table('main_cartitem',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('cart_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('product_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.CheckConstraint('quantity >= 0', name=op.f('main_cartitem_quantity_check')),
    sa.ForeignKeyConstraint(['cart_id'], ['main_cart.id'], name=op.f('main_cartitem_cart_id_8357cf81_fk_main_cart_id'), initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['product_id'], ['main_product.id'], name=op.f('main_cartitem_product_id_777783fc_fk_main_product_id'), initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('main_cartitem_pkey')),
    sa.UniqueConstraint('cart_id', 'product_id', name=op.f('main_cartitem_cart_id_product_id_97f89820_uniq'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_index(op.f('main_cartitem_product_id_777783fc'), 'main_cartitem', ['product_id'], unique=False)
    op.create_index(op.f('main_cartitem_cart_id_8357cf81'), 'main_cartitem', ['cart_id'], unique=False)
    op.create_table('main_category',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('slug', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('image', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('order', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('parent_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['main_category.id'], name='main_category_parent_id_212af219_fk_main_category_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='main_category_pkey'),
    sa.UniqueConstraint('slug', name='main_category_slug_key', postgresql_include=[], postgresql_nulls_not_distinct=False),
    postgresql_ignore_search_path=False
    )
    op.create_index(op.f('main_category_slug_7ae6758d_like'), 'main_category', ['slug'], unique=False)
    op.create_index(op.f('main_category_parent_id_212af219'), 'main_category', ['parent_id'], unique=False)
    op.create_table('main_video',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('thumbnail', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('url', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('embed_url', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('order', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('main_video_pkey'))
    )
    op.create_table('django_admin_log',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('action_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('object_id', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('object_repr', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('action_flag', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('change_message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.CheckConstraint('action_flag >= 0', name=op.f('django_admin_log_action_flag_check')),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name=op.f('django_admin_log_content_type_id_c4bce8eb_fk_django_co'), initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name=op.f('django_admin_log_user_id_c564eba6_fk_auth_user_id'), initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('django_admin_log_pkey'))
    )
    op.create_index(op.f('django_admin_log_user_id_c564eba6'), 'django_admin_log', ['user_id'], unique=False)
    op.create_index(op.f('django_admin_log_content_type_id_c4bce8eb'), 'django_admin_log', ['content_type_id'], unique=False)
    op.create_table('main_subscriber',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=254), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('main_subscriber_pkey')),
    sa.UniqueConstraint('email', name=op.f('main_subscriber_email_key'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_index(op.f('main_subscriber_email_f306f4bd_like'), 'main_subscriber', ['email'], unique=False)
    op.create_table('main_cart',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name=op.f('main_cart_user_id_53cf8b47_fk_auth_user_id'), initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('main_cart_pkey'))
    )
    op.create_index(op.f('main_cart_user_id_53cf8b47'), 'main_cart', ['user_id'], unique=False)
    op.create_table('main_productreview',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('text', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('product_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['main_products.id'], name=op.f('main_productreview_product_id_b0d42925_fk_main_products_id'), initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name=op.f('main_productreview_user_id_bdd4771a_fk_auth_user_id'), initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('main_productreview_pkey'))
    )
    op.create_index(op.f('main_productreview_user_id_bdd4771a'), 'main_productreview', ['user_id'], unique=False)
    op.create_index(op.f('main_productreview_product_id_b0d42925'), 'main_productreview', ['product_id'], unique=False)
    op.create_table('main_product',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('slug', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('short_description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('price', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('image', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('is_popular', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('category_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('order', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.CheckConstraint('"order" >= 0', name=op.f('main_product_order_check')),
    sa.ForeignKeyConstraint(['category_id'], ['main_category.id'], name=op.f('main_product_category_id_c0d90f41_fk_main_category_id'), initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('main_product_pkey')),
    sa.UniqueConstraint('slug', name=op.f('main_product_slug_key'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_index(op.f('main_product_slug_85058272_like'), 'main_product', ['slug'], unique=False)
    op.create_index(op.f('main_product_category_id_c0d90f41'), 'main_product', ['category_id'], unique=False)
    op.create_table('auth_group_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name=op.f('auth_group_permissions_group_id_b120cbf9_fk_auth_group_id'), initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name=op.f('auth_group_permissio_permission_id_84c5c92e_fk_auth_perm'), initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('auth_group_permissions_pkey')),
    sa.UniqueConstraint('group_id', 'permission_id', name=op.f('auth_group_permissions_group_id_permission_id_0cd325b0_uniq'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_index(op.f('auth_group_permissions_permission_id_84c5c92e'), 'auth_group_permissions', ['permission_id'], unique=False)
    op.create_index(op.f('auth_group_permissions_group_id_b120cbf9'), 'auth_group_permissions', ['group_id'], unique=False)
    op.create_table('auth_user_user_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name=op.f('auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm'), initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name=op.f('auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id'), initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('auth_user_user_permissions_pkey')),
    sa.UniqueConstraint('user_id', 'permission_id', name=op.f('auth_user_user_permissions_user_id_permission_id_14a6b632_uniq'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_index(op.f('auth_user_user_permissions_user_id_a95ead1b'), 'auth_user_user_permissions', ['user_id'], unique=False)
    op.create_index(op.f('auth_user_user_permissions_permission_id_1fbb5f2c'), 'auth_user_user_permissions', ['permission_id'], unique=False)
    op.create_table('django_migrations',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('applied', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('django_migrations_pkey'))
    )
    op.create_table('django_session',
    sa.Column('session_key', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('session_data', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('expire_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('session_key', name=op.f('django_session_pkey'))
    )
    op.create_index(op.f('django_session_session_key_c0390e0f_like'), 'django_session', ['session_key'], unique=False)
    op.create_index(op.f('django_session_expire_date_a5c62663'), 'django_session', ['expire_date'], unique=False)
    op.create_table('main_contactmessage',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=254), autoincrement=False, nullable=False),
    sa.Column('message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('is_read', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('main_contactmessage_pkey'))
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('user_pkey'))
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('main_categorys',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('image', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('slug', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('main_categorys_pkey')),
    sa.UniqueConstraint('name', name=op.f('main_categorys_name_fb3ce484_uniq'), postgresql_include=[], postgresql_nulls_not_distinct=False),
    sa.UniqueConstraint('slug', name=op.f('main_categorys_slug_key'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_index(op.f('main_categorys_slug_a2dfb325_like'), 'main_categorys', ['slug'], unique=False)
    op.create_index(op.f('main_categorys_name_fb3ce484_like'), 'main_categorys', ['name'], unique=False)
    # ### end Alembic commands ###
