# Generated by Django 5.1 on 2024-08-19 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campagins', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adgroupdata',
            name='ad_group_metrics',
        ),
        migrations.RemoveField(
            model_name='adgroupdata',
            name='campaign',
        ),
        migrations.RemoveField(
            model_name='keyword',
            name='ad_group',
        ),
        migrations.RemoveField(
            model_name='campaigngoogle',
            name='campaign_budget_details',
        ),
        migrations.RemoveField(
            model_name='campaigngoogle',
            name='campaign_group',
        ),
        migrations.RemoveField(
            model_name='campaigngoogle',
            name='campaign_metrics',
        ),
        migrations.RemoveField(
            model_name='campaigngoogle',
            name='campaign_target_cpa',
        ),
        migrations.RemoveField(
            model_name='keyword',
            name='campaign',
        ),
        migrations.RemoveField(
            model_name='keyword',
            name='keyword_metrics',
        ),
        migrations.CreateModel(
            name='GoogleAnalyticsProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('channel_type', models.CharField(max_length=255)),
                ('property_id', models.CharField(max_length=255, unique=True)),
                ('property_details', models.TextField()),
                ('parent', models.CharField(blank=True, max_length=255, null=True)),
                ('display_name', models.CharField(max_length=255)),
                ('industry_category', models.CharField(choices=[('Ecommerce', 'Ecommerce'), ('SaaS', 'SaaS'), ('Education', 'Education')], max_length=50)),
                ('time_zone', models.CharField(max_length=255)),
                ('currency_code', models.CharField(max_length=10)),
                ('service_level', models.CharField(choices=[('Standard', 'Standard'), ('Premium', 'Premium')], max_length=50)),
                ('account_id', models.CharField(max_length=255)),
            ],
            options={
                'indexes': [models.Index(fields=['property_id'], name='campagins_g_propert_b32b57_idx')],
            },
        ),
        migrations.CreateModel(
            name='GoalMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('goal_completions_all', models.PositiveIntegerField()),
                ('goal_conversion_rate_all', models.DecimalField(decimal_places=2, max_digits=5)),
                ('goal_value_all', models.DecimalField(decimal_places=2, max_digits=20)),
                ('goal_starts_all', models.PositiveIntegerField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_count', models.PositiveIntegerField()),
                ('event_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('event_count_per_user', models.DecimalField(decimal_places=2, max_digits=10)),
                ('events_per_session', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EngagementMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('average_session_duration', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bounce_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('engagement_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('screen_page_views', models.PositiveIntegerField()),
                ('engaged_sessions_per_user', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user_engagement_duration', models.PositiveIntegerField()),
                ('screen_page_views_per_session', models.DecimalField(decimal_places=2, max_digits=5)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engagement_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EcommerceMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('purchase_revenue', models.DecimalField(decimal_places=2, max_digits=20)),
                ('transactions', models.PositiveIntegerField()),
                ('purchase_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('average_purchase_revenue', models.DecimalField(decimal_places=2, max_digits=20)),
                ('refund_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('average_purchase_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('ecommerce_purchases', models.PositiveIntegerField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ecommerce_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DemographicMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('device_category', models.CharField(max_length=255)),
                ('operating_system', models.CharField(max_length=255)),
                ('browser', models.CharField(max_length=255)),
                ('screen_resolution', models.CharField(max_length=255)),
                ('app_version', models.CharField(max_length=255)),
                ('platform', models.CharField(max_length=255)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demographic_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('page_views', models.PositiveIntegerField()),
                ('unique_page_views', models.PositiveIntegerField()),
                ('time_on_page', models.DecimalField(decimal_places=2, max_digits=10)),
                ('entrances', models.PositiveIntegerField()),
                ('page_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('exit_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ad_clicks', models.PositiveIntegerField()),
                ('ad_cost', models.DecimalField(decimal_places=2, max_digits=20)),
                ('ad_impressions', models.PositiveIntegerField()),
                ('ad_revenue', models.DecimalField(decimal_places=2, max_digits=20)),
                ('return_on_ad_spend', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ad_cost_per_click', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ad_click_through_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LifetimeValueMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lifetime_value_revenue', models.DecimalField(decimal_places=2, max_digits=20)),
                ('lifetime_value_purchases', models.PositiveIntegerField()),
                ('average_lifetime_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('customer_lifetime_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lifetime_value_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PovitMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sessions', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('country', models.CharField(max_length=255)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='povit_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RealtimeMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(max_length=255)),
                ('active_users', models.PositiveIntegerField()),
                ('screen_page_views', models.PositiveIntegerField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realtime_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SessionMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sessions', models.PositiveIntegerField()),
                ('engaged_sessions', models.PositiveIntegerField()),
                ('sessions_per_user', models.DecimalField(decimal_places=2, max_digits=5)),
                ('average_session_duration', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bounce_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('engagement_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('session_duration_per_user', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TechnologyMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('device_category', models.CharField(max_length=255)),
                ('operating_system', models.CharField(max_length=255)),
                ('browser', models.CharField(max_length=255)),
                ('screen_resolution', models.CharField(max_length=255)),
                ('app_version', models.CharField(max_length=255)),
                ('platform', models.CharField(max_length=255)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technology_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active_users', models.PositiveIntegerField()),
                ('new_users', models.PositiveIntegerField()),
                ('total_users', models.PositiveIntegerField()),
                ('crash_free_users_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('crash_affected_users', models.PositiveIntegerField()),
                ('user_engagement_duration', models.PositiveIntegerField()),
                ('user_stickiness', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user_retention', models.DecimalField(decimal_places=2, max_digits=5)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UTMParamsMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('source', models.CharField(max_length=255)),
                ('medium', models.CharField(max_length=255)),
                ('campaign', models.CharField(max_length=255)),
                ('term', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('sessions', models.PositiveIntegerField()),
                ('users', models.PositiveIntegerField()),
                ('page_views', models.PositiveIntegerField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utm_params_metrics', to='campagins.googleanalyticsproperty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='AdData',
        ),
        migrations.DeleteModel(
            name='AdGroupMetrics',
        ),
        migrations.DeleteModel(
            name='AdGroupData',
        ),
        migrations.DeleteModel(
            name='CampaignBudgetDetails',
        ),
        migrations.DeleteModel(
            name='CampaignGroup',
        ),
        migrations.DeleteModel(
            name='CampaignMetrics',
        ),
        migrations.DeleteModel(
            name='CampaignTargetCpa',
        ),
        migrations.DeleteModel(
            name='CampaignGoogle',
        ),
        migrations.DeleteModel(
            name='Keyword',
        ),
        migrations.DeleteModel(
            name='Metrics',
        ),
    ]
