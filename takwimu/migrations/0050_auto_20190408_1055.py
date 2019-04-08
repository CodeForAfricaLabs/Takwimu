# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-08 07:55
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('takwimu', '0049_indexpage_featured_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpage',
            name='featured_analysis',
            field=wagtail.core.fields.StreamField([('featured_analysis', wagtail.core.blocks.StructBlock([('featured_page', wagtail.core.blocks.PageChooserBlock(target_model=['takwimu.ProfileSectionPage'])), ('from_country', wagtail.core.blocks.ChoiceBlock(choices=[('BF', 'Burkina Faso'), ('CD', 'Democratic Republic of Congo'), ('ET', 'Ethiopia'), ('KE', 'Kenya'), ('NG', 'Nigeria'), ('SN', 'Senegal'), ('ZA', 'South Africa'), ('TZ', 'Tanzania'), ('UG', 'Uganda'), ('ZM', 'Zambia')]))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='featured_data',
            field=wagtail.core.fields.StreamField([('featured_data', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('country', wagtail.core.blocks.ChoiceBlock(choices=[('ET', 'Ethiopia'), ('KE', 'Kenya'), ('NG', 'Nigeria'), ('SN', 'Senegal'), ('TZ', 'Tanzania')], label='Country')), ('data_id', wagtail.core.blocks.ChoiceBlock(choices=[('demographics-residence_dist', 'Population by Residence'), ('demographics-sex_dist', 'Population by Sex'), ('crops-crop_distribution', 'Crops Produced'), ('health_centers-prevention_methods_dist', 'Knowledge of HIV Prevention Methods'), ('education-education_reached_distribution', 'Highest Level of Education Attained'), ('education-school_attendance_distribution', 'School Attendance by Sex'), ('donors-donor_assistance_dist', 'Principal Donors'), ('poverty-poverty_residence_dist', 'Percentage of Population living in Poverty by Residence'), ('poverty-poverty_age_dist', 'Percentage of Population living in Poverty by Age and Residence'), ('fgm-fgm_age_dist', 'Percentage of Women that have undergone FGM by Age'), ('security-seized_firearms_dist', 'Seized Firearms'), ('donors-donor_programmes_dist', 'Donor Funded Programmes'), ('budget-government_expenditure_dist', 'Government Expenditure'), ('health_centers-health_centers_dist', 'Number of health centers by type')], label='Data')), ('chart_type', wagtail.core.blocks.ChoiceBlock(choices=[('histogram', 'Histogram'), ('pie', 'Pie Chart'), ('grouped_column', 'Grouped Column')], label='Chart Type')), ('data_stat_type', wagtail.core.blocks.ChoiceBlock(choices=[('percentage', 'Percentage'), ('scaled-percentage', 'Scaled Percentage'), ('dollar', 'Dollar')], label='Stat Type')), ('chart_height', wagtail.core.blocks.IntegerBlock(help_text='Default is 300px', label='Chart Height', required=False)), ('description', wagtail.core.blocks.TextBlock(label='Description of the data', required=False))]))], blank=True),
        ),
    ]
