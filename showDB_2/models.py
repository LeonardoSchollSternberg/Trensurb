# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Branch(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    branch_name = models.CharField(max_length=40, blank=True, null=True)
    mgr = models.ForeignKey('Employee', models.DO_NOTHING, blank=True, null=True)
    mgr_start_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branch'


class BranchSupplier(models.Model):
    branch = models.OneToOneField(Branch, models.DO_NOTHING, primary_key=True)
    supplier_name = models.CharField(max_length=40)
    supply_type = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branch_supplier'
        unique_together = (('branch', 'supplier_name'),)


class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=40, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    super = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class PrintTeste2(models.Model):
    message = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'print_teste_2'


class Teste3(models.Model):
    criado_em = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teste_3'


class TriggerTest(models.Model):
    message = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trigger_test'


class WorksWith(models.Model):
    emp = models.OneToOneField(Employee, models.DO_NOTHING, primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    total_sales = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'works_with'
        unique_together = (('emp', 'client'),)
