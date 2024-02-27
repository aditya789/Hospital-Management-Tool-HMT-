# Generated by Django 5.0.2 on 2024-02-27 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmt_main_app', '0005_rename_homepages_homepage_delete_keyval'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='cleanliness_header',
            field=models.TextField(default='We Maintain Cleanliness Rules Inside Our Hospital'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='cleanliness_tagline',
            field=models.TextField(default='Our Hospital cleanliness is upheld through rigorous disinfection protocols and strict hand hygiene measures. Continuous monitoring ensures a safe and hygienic environment for patients and staff.'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='emergency_call_header',
            field=models.TextField(default='Do you need Emergency Medical Care? Call @'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='emergency_call_tagline',
            field=models.TextField(default='We ensure immediate response to critical situations, providing life-saving interventions and rapid transport to healthcare facilities. Highly trained professionals deliver urgent medical assistance, prioritizing patient stabilization and timely treatment.'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='scheduler_3_tagline',
            field=models.TextField(default="<li class='day'>Monday<span>9AM - 6PM</span></li><li class='day'>Tuesday<span>9AM - 6PM</span></li><li class='day'>Wednesday<span>9AM - 6PM</span></li><li class='day'>Thursday<span>9AM - 6PM</span></li><li class='day'>Firday<span>9AM - 6PM</span></li><li class='day'>Saturday<span>9AM - 6PM</span></li><li class='day'>Sunday <span>9AM - 12PM</span></li>"),
        ),
    ]
