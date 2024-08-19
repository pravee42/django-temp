# Generated by Django 5.1 on 2024-08-19 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdGroupMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_micros', models.BigIntegerField()),
                ('conversions_value', models.DecimalField(decimal_places=6, max_digits=20)),
                ('clicks', models.IntegerField()),
                ('interaction_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('view_through_conversions', models.IntegerField()),
                ('average_cpc', models.BigIntegerField()),
                ('conversions', models.DecimalField(decimal_places=6, max_digits=20)),
                ('ctr', models.DecimalField(decimal_places=2, max_digits=5)),
                ('all_conversions_value', models.DecimalField(decimal_places=6, max_digits=20)),
                ('conversions_from_interactions_rate', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignBudgetDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_id', models.CharField(max_length=250, unique=True)),
                ('budget_name', models.CharField(max_length=250)),
                ('period', models.CharField(choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly')], max_length=50)),
                ('amount_micros', models.BigIntegerField()),
                ('status', models.CharField(max_length=250)),
                ('recommended_budget_estimated_change_weekly_views', models.IntegerField()),
                ('recommended_budget_estimated_change_weekly_interactions', models.IntegerField()),
                ('recommended_budget_estimated_change_weekly_cost_micros', models.BigIntegerField()),
                ('recommended_budget_estimated_change_weekly_clicks', models.IntegerField()),
                ('recommended_budget_amount_micros', models.BigIntegerField()),
                ('campaign_budget_type', models.CharField(max_length=250)),
                ('total_amount_micros', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CampaignGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.CharField(max_length=250, unique=True)),
                ('group_name', models.CharField(max_length=250)),
                ('resource_name', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_micros', models.BigIntegerField()),
                ('conversions_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('clicks', models.IntegerField()),
                ('interaction_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('view_through_conversions', models.IntegerField()),
                ('average_cpc', models.BigIntegerField()),
                ('conversions', models.IntegerField()),
                ('ctr', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cost_per_conversion', models.BigIntegerField()),
                ('value_per_conversion', models.BigIntegerField()),
                ('all_conversions_value', models.BigIntegerField()),
                ('conversions_from_interactions_rate', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignTargetCpa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpc_bid_ceiling_micros', models.BigIntegerField()),
                ('cpc_bid_floor_micros', models.BigIntegerField()),
                ('target_cpa_micros', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_micros', models.BigIntegerField()),
                ('conversion_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('clicks', models.IntegerField()),
                ('interaction_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('view_through_conversions', models.IntegerField()),
                ('average_cpc', models.BigIntegerField()),
                ('conversions', models.DecimalField(decimal_places=2, max_digits=20)),
                ('ctr', models.DecimalField(decimal_places=2, max_digits=5)),
                ('all_conversions', models.IntegerField()),
                ('cost_per_conversions', models.BigIntegerField()),
                ('value_per_conversion', models.BigIntegerField()),
                ('all_conversions_value', models.BigIntegerField()),
                ('conversions_from_interactions_rate', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignGoogle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_id', models.CharField(db_index=True, max_length=250, unique=True)),
                ('campaign_name', models.CharField(db_index=True, max_length=250)),
                ('campaign_status', models.CharField(choices=[('ENABLED', 'Enabled'), ('PAUSED', 'Paused'), ('REMOVED', 'Removed')], max_length=50)),
                ('campaign_serving_status', models.CharField(max_length=250)),
                ('campaign_advertising_channel_type', models.CharField(max_length=250)),
                ('campaign_start_date', models.DateField()),
                ('campaign_end_date', models.DateField(blank=True, null=True)),
                ('campaign_budget', models.BigIntegerField()),
                ('campaign_budget_details', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='campagins.campaignbudgetdetails')),
                ('campaign_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='campagins.campaigngroup')),
                ('campaign_metrics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campagins.campaignmetrics')),
                ('campaign_target_cpa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='campagins.campaigntargetcpa')),
            ],
            options={
                'verbose_name': 'Google Campaign',
                'verbose_name_plural': 'Google Campaigns',
                'ordering': ['campaign_name'],
            },
        ),
        migrations.CreateModel(
            name='AdGroupData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_group_id', models.CharField(max_length=250, unique=True)),
                ('ad_group_name', models.CharField(max_length=250)),
                ('effective_target_cpa_micros', models.BigIntegerField()),
                ('ad_group_type', models.CharField(max_length=100)),
                ('target_cpm_micros', models.BigIntegerField()),
                ('target_cpa_micros', models.BigIntegerField()),
                ('ad_group_metrics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campagins.adgroupmetrics')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campagins.campaigngoogle')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=250, unique=True)),
                ('keyword_text', models.CharField(max_length=250)),
                ('keyword_match_type', models.CharField(max_length=250)),
                ('ad_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campagins.adgroupdata')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campagins.campaigngoogle')),
                ('keyword_metrics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keyword_metrics', to='campagins.metrics')),
            ],
        ),
        migrations.CreateModel(
            name='AdData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_id', models.CharField(max_length=250, unique=True)),
                ('ad_name', models.CharField(max_length=250)),
                ('ad_status', models.CharField(max_length=250)),
                ('final_urls', models.CharField(max_length=250)),
                ('description1', models.CharField(max_length=250)),
                ('description2', models.CharField(max_length=250)),
                ('ad_type', models.CharField(max_length=250)),
                ('ad_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campagins.adgroupdata')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campagins.campaigngoogle')),
                ('ad_metrics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_metrics', to='campagins.metrics')),
            ],
        ),
    ]
