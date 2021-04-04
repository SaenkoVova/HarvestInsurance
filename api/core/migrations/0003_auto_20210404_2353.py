# Generated by Django 3.1.7 on 2021-04-04 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210311_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('docid', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('passportissue', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'doc',
            },
        ),
        migrations.CreateModel(
            name='Insuredevent',
            fields=[
                ('description', models.CharField(blank=True, max_length=20, null=True)),
                ('hint', models.CharField(blank=True, max_length=20, null=True)),
                ('eventid', models.IntegerField(primary_key=True, serialize=False)),
                ('impactprice', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'insuredevent',
            },
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('policeid', models.IntegerField(primary_key=True, serialize=False)),
                ('geojson', models.CharField(blank=True, max_length=20, null=True)),
                ('cadastralnumber', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('term', models.IntegerField(blank=True, null=True)),
                ('coating', models.IntegerField(blank=True, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'police',
            },
        ),
        migrations.AlterModelOptions(
            name='client',
            options={},
        ),
        migrations.RemoveField(
            model_name='client',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.RemoveField(
            model_name='client',
            name='passport',
        ),
        migrations.RemoveField(
            model_name='client',
            name='secondName',
        ),
        migrations.AddField(
            model_name='client',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='clientid',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='firstname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='secondname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='thirdname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterModelTable(
            name='client',
            table='client',
        ),
        migrations.CreateModel(
            name='Foreignpassport',
            fields=[
                ('seriesandnumber', models.CharField(blank=True, max_length=20, null=True)),
                ('docid', models.OneToOneField(db_column='docid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.doc')),
                ('clientid', models.IntegerField()),
            ],
            options={
                'db_table': 'foreignpassport',
                'unique_together': {('docid', 'clientid')},
            },
        ),
        migrations.CreateModel(
            name='Idcard',
            fields=[
                ('issuedby', models.CharField(blank=True, max_length=20, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('notation', models.CharField(blank=True, max_length=20, null=True)),
                ('docid', models.OneToOneField(db_column='docid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.doc')),
                ('clientid', models.IntegerField()),
            ],
            options={
                'db_table': 'idcard',
                'unique_together': {('docid', 'clientid')},
            },
        ),
        migrations.CreateModel(
            name='Ukrainepassport',
            fields=[
                ('seriesandnumber', models.CharField(blank=True, max_length=20, null=True)),
                ('issuedby', models.DateField(blank=True, null=True)),
                ('docid', models.OneToOneField(db_column='docid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.doc')),
                ('clientid', models.IntegerField()),
            ],
            options={
                'db_table': 'ukrainepassport',
                'unique_together': {('docid', 'clientid')},
            },
        ),
        migrations.DeleteModel(
            name='Field',
        ),
        migrations.AddField(
            model_name='police',
            name='clientid',
            field=models.ForeignKey(blank=True, db_column='clientid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.client'),
        ),
        migrations.AddField(
            model_name='doc',
            name='clientid',
            field=models.ForeignKey(db_column='clientid', on_delete=django.db.models.deletion.DO_NOTHING, to='core.client'),
        ),
        migrations.AlterUniqueTogether(
            name='doc',
            unique_together={('docid', 'clientid')},
        ),
    ]
