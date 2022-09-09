# Generated by Django 3.2.15 on 2022-09-13 03:03
# flake8: noqa

from django.db import migrations
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0002_auto_20220808_1420"),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name="custommodel",
            name="int_field_updated",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="custommodel",
            name="snapshot_insert",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="custommodel",
            name="snapshot_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="eventmodel",
            name="model_create",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="eventmodel",
            name="before_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="eventmodel",
            name="before_delete",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="eventmodel",
            name="after_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="eventmodel",
            name="model_custom_create",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="no_pgh_obj_snapshot_insert",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="no_pgh_obj_snapshot_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="snapshot_insert",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="snapshot_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="dt_field_int_field_snapshot_insert",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="dt_field_int_field_snapshot_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="dt_field_snapshot_insert",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="dt_field_snapshot_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="custom_snapshot_insert",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="snapshotmodel",
            name="custom_snapshot_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="uniqueconstraintmodel",
            name="snapshot_insert",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="uniqueconstraintmodel",
            name="snapshot_update",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="usergroups",
            name="group_add",
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name="usergroups",
            name="group_remove",
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="custommodel",
            trigger=pgtrigger.compiler.Trigger(
                name="int_field_updated",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."integer_field" IS DISTINCT FROM NEW."integer_field")',
                    func='INSERT INTO "tests_custommodelevent" ("integer_field", "my_pk", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."integer_field", NEW."my_pk", _pgh_attach_context(), NOW(), \'int_field_updated\', NEW."my_pk"); RETURN NULL;',
                    hash="27914f913dc211bd459c9df206abad31bf36e2e7",
                    operation="UPDATE",
                    pgid="pgtrigger_int_field_updated_a1031",
                    table="tests_custommodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="custommodel",
            trigger=pgtrigger.compiler.Trigger(
                name="snapshot_insert",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_custommodelsnapshot" ("integer_field", "my_pk", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."integer_field", NEW."my_pk", _pgh_attach_context(), NOW(), \'snapshot\', NEW."my_pk"); RETURN NULL;',
                    hash="ea6e97ef362cc952bcee7b6f712f04ace92b3ae0",
                    operation="INSERT",
                    pgid="pgtrigger_snapshot_insert_16a4e",
                    table="tests_custommodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="custommodel",
            trigger=pgtrigger.compiler.Trigger(
                name="snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."my_pk" IS DISTINCT FROM NEW."my_pk" OR OLD."integer_field" IS DISTINCT FROM NEW."integer_field")',
                    func='INSERT INTO "tests_custommodelsnapshot" ("integer_field", "my_pk", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."integer_field", NEW."my_pk", _pgh_attach_context(), NOW(), \'snapshot\', NEW."my_pk"); RETURN NULL;',
                    hash="67a767014d9e810ea6e7d3208d6db1a78817ca6b",
                    operation="UPDATE",
                    pgid="pgtrigger_snapshot_update_47d37",
                    table="tests_custommodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="eventmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="model_create",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_eventmodelevent" ("dt_field", "id", "int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."dt_field", NEW."id", NEW."int_field", _pgh_attach_context(), NOW(), \'model.create\', NEW."id"); RETURN NULL;',
                    hash="5d350ae78918528c0e1f9c48468536489b262413",
                    operation="INSERT",
                    pgid="pgtrigger_model_create_bc0bd",
                    table="tests_eventmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="eventmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="before_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_eventmodelevent" ("dt_field", "id", "int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (OLD."dt_field", OLD."id", OLD."int_field", _pgh_attach_context(), NOW(), \'before_update\', OLD."id"); RETURN NULL;',
                    hash="5f516e3c39bf7debb5f9a73b6592904135ab9da5",
                    operation="UPDATE",
                    pgid="pgtrigger_before_update_aad5f",
                    table="tests_eventmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="eventmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="before_delete",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_eventmodelevent" ("dt_field", "id", "int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (OLD."dt_field", OLD."id", OLD."int_field", _pgh_attach_context(), NOW(), \'before_delete\', OLD."id"); RETURN NULL;',
                    hash="1f63db5e601f13db9da8be1bfd884faaf7e04e6a",
                    operation="DELETE",
                    pgid="pgtrigger_before_delete_d022b",
                    table="tests_eventmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="eventmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="after_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."dt_field" IS DISTINCT FROM NEW."dt_field")',
                    func='INSERT INTO "tests_eventmodelevent" ("dt_field", "id", "int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."dt_field", NEW."id", NEW."int_field", _pgh_attach_context(), NOW(), \'after_update\', NEW."id"); RETURN NULL;',
                    hash="3330db56b51bca0d84933627c942bab95eada0fa",
                    operation="UPDATE",
                    pgid="pgtrigger_after_update_5b8c8",
                    table="tests_eventmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="eventmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="model_custom_create",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_customeventmodel" ("dt_field", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."dt_field", NOW(), \'model.custom_create\', NEW."id"); RETURN NULL;',
                    hash="e8050df11c17466e96ea48242b2f05785a142744",
                    operation="INSERT",
                    pgid="pgtrigger_model_custom_create_78c73",
                    table="tests_eventmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="no_pgh_obj_snapshot_insert",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_nopghobjsnapshot" ("dt_field", "fk_field_id", "id", "int_field", "pgh_context_id", "pgh_created_at", "pgh_label") VALUES (NEW."dt_field", NEW."fk_field_id", NEW."id", NEW."int_field", _pgh_attach_context(), NOW(), \'no_pgh_obj_snapshot\'); RETURN NULL;',
                    hash="f2a163a9493a2c1a6c990e603a5e39b33ae99528",
                    operation="INSERT",
                    pgid="pgtrigger_no_pgh_obj_snapshot_insert_d3501",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="no_pgh_obj_snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."id" IS DISTINCT FROM NEW."id" OR OLD."dt_field" IS DISTINCT FROM NEW."dt_field" OR OLD."int_field" IS DISTINCT FROM NEW."int_field" OR OLD."fk_field_id" IS DISTINCT FROM NEW."fk_field_id")',
                    func='INSERT INTO "tests_nopghobjsnapshot" ("dt_field", "fk_field_id", "id", "int_field", "pgh_context_id", "pgh_created_at", "pgh_label") VALUES (NEW."dt_field", NEW."fk_field_id", NEW."id", NEW."int_field", _pgh_attach_context(), NOW(), \'no_pgh_obj_snapshot\'); RETURN NULL;',
                    hash="2fa346ad4c75e472f1dac84595c93e165c1d55fc",
                    operation="UPDATE",
                    pgid="pgtrigger_no_pgh_obj_snapshot_update_015b7",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="snapshot_insert",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_snapshotmodelsnapshot" ("dt_field", "fk_field_id", "id", "int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."dt_field", NEW."fk_field_id", NEW."id", NEW."int_field", _pgh_attach_context(), NOW(), \'snapshot\', NEW."id"); RETURN NULL;',
                    hash="efb4176833983d7608c75df4470f16689c38d9fe",
                    operation="INSERT",
                    pgid="pgtrigger_snapshot_insert_287a7",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."id" IS DISTINCT FROM NEW."id" OR OLD."dt_field" IS DISTINCT FROM NEW."dt_field" OR OLD."int_field" IS DISTINCT FROM NEW."int_field" OR OLD."fk_field_id" IS DISTINCT FROM NEW."fk_field_id")',
                    func='INSERT INTO "tests_snapshotmodelsnapshot" ("dt_field", "fk_field_id", "id", "int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."dt_field", NEW."fk_field_id", NEW."id", NEW."int_field", _pgh_attach_context(), NOW(), \'snapshot\', NEW."id"); RETURN NULL;',
                    hash="324af4590ff3132007e716fa637cdf485200f372",
                    operation="UPDATE",
                    pgid="pgtrigger_snapshot_update_4041c",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="dt_field_int_field_snapshot_insert",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_snapshotmodeldtfieldintfieldevent" ("dt_field", "int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."dt_field", NEW."int_field", _pgh_attach_context(), NOW(), \'dt_field_int_field_snapshot\', NEW."id"); RETURN NULL;',
                    hash="685d7303c58ebf04c05b14eeda6490a576966b09",
                    operation="INSERT",
                    pgid="pgtrigger_dt_field_int_field_snapshot_insert_85480",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="dt_field_int_field_snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."dt_field" IS DISTINCT FROM NEW."dt_field" OR OLD."int_field" IS DISTINCT FROM NEW."int_field")',
                    func='INSERT INTO "tests_snapshotmodeldtfieldintfieldevent" ("dt_field", "int_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."dt_field", NEW."int_field", _pgh_attach_context(), NOW(), \'dt_field_int_field_snapshot\', NEW."id"); RETURN NULL;',
                    hash="4d377399a19b3ae77ff226961197a38617f2fc11",
                    operation="UPDATE",
                    pgid="pgtrigger_dt_field_int_field_snapshot_update_8246d",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="dt_field_snapshot_insert",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_snapshotmodeldtfieldevent" ("dt_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."dt_field", _pgh_attach_context(), NOW(), \'dt_field_snapshot\', NEW."id"); RETURN NULL;',
                    hash="53f21a43f3c426cf97087eeb06a6ed1270bb6a33",
                    operation="INSERT",
                    pgid="pgtrigger_dt_field_snapshot_insert_f46b8",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="dt_field_snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."dt_field" IS DISTINCT FROM NEW."dt_field")',
                    func='INSERT INTO "tests_snapshotmodeldtfieldevent" ("dt_field", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."dt_field", _pgh_attach_context(), NOW(), \'dt_field_snapshot\', NEW."id"); RETURN NULL;',
                    hash="31bab347c9e5c370c5637644013c0e9a691dc365",
                    operation="UPDATE",
                    pgid="pgtrigger_dt_field_snapshot_update_22f55",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="custom_snapshot_insert",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_customsnapshotmodel" ("fk_field_id", "id", "int_field", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."fk_field_id", NEW."id", NEW."int_field", NOW(), \'custom_snapshot\', NEW."id"); RETURN NULL;',
                    hash="589e0126974e6cd052906ed20829c2a28c7c9faa",
                    operation="INSERT",
                    pgid="pgtrigger_custom_snapshot_insert_6d300",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="snapshotmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="custom_snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."id" IS DISTINCT FROM NEW."id" OR OLD."int_field" IS DISTINCT FROM NEW."int_field" OR OLD."fk_field_id" IS DISTINCT FROM NEW."fk_field_id")',
                    func='INSERT INTO "tests_customsnapshotmodel" ("fk_field_id", "id", "int_field", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."fk_field_id", NEW."id", NEW."int_field", NOW(), \'custom_snapshot\', NEW."id"); RETURN NULL;',
                    hash="f92a06b7747d0a2e649c8f39be8d917052dc7da7",
                    operation="UPDATE",
                    pgid="pgtrigger_custom_snapshot_update_5af3e",
                    table="tests_snapshotmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="uniqueconstraintmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="snapshot_insert",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_uniqueconstraintmodelevent" ("id", "my_char_field", "my_int_field1", "my_int_field2", "my_one_to_one_id", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."id", NEW."my_char_field", NEW."my_int_field1", NEW."my_int_field2", NEW."my_one_to_one_id", _pgh_attach_context(), NOW(), \'snapshot\', NEW."id"); RETURN NULL;',
                    hash="4581b70b015ec980e1f735c45ca02014cedce673",
                    operation="INSERT",
                    pgid="pgtrigger_snapshot_insert_ed815",
                    table="tests_uniqueconstraintmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="uniqueconstraintmodel",
            trigger=pgtrigger.compiler.Trigger(
                name="snapshot_update",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    condition='WHEN (OLD."id" IS DISTINCT FROM NEW."id" OR OLD."my_one_to_one_id" IS DISTINCT FROM NEW."my_one_to_one_id" OR OLD."my_char_field" IS DISTINCT FROM NEW."my_char_field" OR OLD."my_int_field1" IS DISTINCT FROM NEW."my_int_field1" OR OLD."my_int_field2" IS DISTINCT FROM NEW."my_int_field2")',
                    func='INSERT INTO "tests_uniqueconstraintmodelevent" ("id", "my_char_field", "my_int_field1", "my_int_field2", "my_one_to_one_id", "pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id") VALUES (NEW."id", NEW."my_char_field", NEW."my_int_field1", NEW."my_int_field2", NEW."my_one_to_one_id", _pgh_attach_context(), NOW(), \'snapshot\', NEW."id"); RETURN NULL;',
                    hash="d5e02981b7ca67c416a83c38d5caa743b888a9e9",
                    operation="UPDATE",
                    pgid="pgtrigger_snapshot_update_9e83c",
                    table="tests_uniqueconstraintmodel",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="usergroups",
            trigger=pgtrigger.compiler.Trigger(
                name="group_add",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_usergroupsevent" ("group_id", "id", "pgh_context_id", "pgh_created_at", "pgh_label", "user_id") VALUES (NEW."group_id", NEW."id", _pgh_attach_context(), NOW(), \'group.add\', NEW."user_id"); RETURN NULL;',
                    hash="a2f18ef00bcad3fad2f68a89dde18ad17ca4022c",
                    operation="INSERT",
                    pgid="pgtrigger_group_add_9d386",
                    table="auth_user_groups",
                    when="AFTER",
                ),
            ),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name="usergroups",
            trigger=pgtrigger.compiler.Trigger(
                name="group_remove",
                sql=pgtrigger.compiler.UpsertTriggerSql(
                    func='INSERT INTO "tests_usergroupsevent" ("group_id", "id", "pgh_context_id", "pgh_created_at", "pgh_label", "user_id") VALUES (OLD."group_id", OLD."id", _pgh_attach_context(), NOW(), \'group.remove\', OLD."user_id"); RETURN NULL;',
                    hash="5ac3c434d94dbe50d890ab27134248197af1e392",
                    operation="DELETE",
                    pgid="pgtrigger_group_remove_4d892",
                    table="auth_user_groups",
                    when="AFTER",
                ),
            ),
        ),
    ]
