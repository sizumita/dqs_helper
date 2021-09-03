from django.db import models


class QuestionInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    original_message_id = models.BigIntegerField(blank=True, null=True)
    info_message_id = models.BigIntegerField(blank=True, null=True)
    question = models.OneToOneField('Questions', models.DO_NOTHING, blank=True, null=True)
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'question_info'

    def __str__(self):
        return self.question.name


class Questions(models.Model):
    id = models.BigAutoField(primary_key=True)
    issuer_id = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    channel_id = models.BigIntegerField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)  # This field type is a guess.
    inserted_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'questions'

    def __str__(self):
        return self.name


class SchemaMigrations(models.Model):
    version = models.BigIntegerField(primary_key=True)
    inserted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schema_migrations'
