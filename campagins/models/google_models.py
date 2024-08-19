from django.db import models

# Choices for specific fields
CAMPAIGN_STATUS_CHOICES = [
    ('ENABLED', 'Enabled'),
    ('PAUSED', 'Paused'),
    ('REMOVED', 'Removed'),
]

BUDGET_PERIOD_CHOICES = [
    ('DAILY', 'Daily'),
    ('WEEKLY', 'Weekly'),
    ('MONTHLY', 'Monthly'),
]

class CampaignTargetCpa(models.Model):
    cpc_bid_ceiling_micros = models.BigIntegerField()
    cpc_bid_floor_micros = models.BigIntegerField()
    target_cpa_micros = models.BigIntegerField()

    def __str__(self):
        return f"Target CPA: {self.target_cpa_micros}"

class CampaignBudgetDetails(models.Model):
    budget_id = models.CharField(max_length=250, unique=True)
    budget_name = models.CharField(max_length=250)
    period = models.CharField(max_length=50, choices=BUDGET_PERIOD_CHOICES)
    amount_micros = models.BigIntegerField()
    status = models.CharField(max_length=250)
    recommended_budget_estimated_change_weekly_views = models.IntegerField()
    recommended_budget_estimated_change_weekly_interactions = models.IntegerField()
    recommended_budget_estimated_change_weekly_cost_micros = models.BigIntegerField()
    recommended_budget_estimated_change_weekly_clicks = models.IntegerField()
    recommended_budget_amount_micros = models.BigIntegerField()
    campaign_budget_type = models.CharField(max_length=250)
    total_amount_micros = models.BigIntegerField()

    def __str__(self):
        return self.budget_name

class CampaignGroup(models.Model):
    group_id = models.CharField(max_length=250, unique=True)
    group_name = models.CharField(max_length=250)
    resource_name = models.CharField(max_length=250)
    status = models.CharField(max_length=250)

    def __str__(self):
        return self.group_name

class CampaignMetrics(models.Model):
    cost_micros = models.BigIntegerField()
    conversions_value = models.DecimalField(max_digits=20, decimal_places=2)
    clicks = models.IntegerField()
    interaction_rate = models.DecimalField(max_digits=5, decimal_places=2)
    view_through_conversions = models.IntegerField()
    average_cpc = models.BigIntegerField()
    conversions = models.IntegerField()
    ctr = models.DecimalField(max_digits=5, decimal_places=2)
    cost_per_conversion = models.BigIntegerField()
    value_per_conversion = models.BigIntegerField()
    all_conversions_value = models.BigIntegerField()
    conversions_from_interactions_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Metrics for {self.cost_micros} cost micros"

class CampaignGoogle(models.Model):
    campaign_id = models.CharField(max_length=250, unique=True, db_index=True)
    campaign_name = models.CharField(max_length=250, db_index=True)
    campaign_status = models.CharField(max_length=50, choices=CAMPAIGN_STATUS_CHOICES)
    campaign_serving_status = models.CharField(max_length=250)
    campaign_advertising_channel_type = models.CharField(max_length=250)
    campaign_start_date = models.DateField()
    campaign_end_date = models.DateField(null=True, blank=True)
    campaign_budget = models.BigIntegerField()
    campaign_target_cpa = models.ForeignKey(CampaignTargetCpa, on_delete=models.PROTECT)
    campaign_budget_details = models.ForeignKey(CampaignBudgetDetails, on_delete=models.PROTECT)
    campaign_group = models.ForeignKey(CampaignGroup, on_delete=models.PROTECT)
    campaign_metrics = models.ForeignKey(CampaignMetrics, on_delete=models.CASCADE)

    class Meta:
        ordering = ['campaign_name']
        verbose_name = 'Google Campaign'
        verbose_name_plural = 'Google Campaigns'

    def __str__(self):
        return self.campaign_name

class AdGroupMetrics(models.Model):
    cost_micros = models.BigIntegerField()
    conversions_value = models.DecimalField(max_digits=20, decimal_places=6)
    clicks = models.IntegerField()
    interaction_rate = models.DecimalField(max_digits=5, decimal_places=2)
    view_through_conversions = models.IntegerField()
    average_cpc = models.BigIntegerField()
    conversions = models.DecimalField(max_digits=20, decimal_places=6)
    ctr = models.DecimalField(max_digits=5, decimal_places=2)
    all_conversions_value = models.DecimalField(max_digits=20, decimal_places=6)
    conversions_from_interactions_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Metrics for AdGroup with cost: {self.cost_micros} micros"

class AdGroupData(models.Model):
    ad_group_id = models.CharField(max_length=250, unique=True)
    ad_group_name = models.CharField(max_length=250)
    campaign = models.ForeignKey(CampaignGoogle, on_delete=models.CASCADE)
    effective_target_cpa_micros = models.BigIntegerField()
    ad_group_type = models.CharField(max_length=100)
    target_cpm_micros = models.BigIntegerField()
    target_cpa_micros = models.BigIntegerField()
    ad_group_metrics = models.ForeignKey(AdGroupMetrics, on_delete=models.CASCADE)

    def __str__(self):
        return self.ad_group_name

class Metrics(models.Model):
    cost_micros = models.BigIntegerField()
    conversion_value = models.DecimalField(max_digits=20, decimal_places=2)
    clicks = models.IntegerField()
    interaction_rate = models.DecimalField(max_digits=5, decimal_places=2)
    view_through_conversions = models.IntegerField()
    average_cpc = models.BigIntegerField()
    conversions = models.DecimalField(max_digits=20, decimal_places=2)
    ctr = models.DecimalField(max_digits=5, decimal_places=2)
    all_conversions = models.IntegerField()
    cost_per_conversions = models.BigIntegerField()
    value_per_conversion = models.BigIntegerField()
    all_conversions_value = models.BigIntegerField()
    conversions_from_interactions_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Metrics with cost: {self.cost_micros}"

class AdData(models.Model):
    ad_id = models.CharField(max_length=250, unique=True)
    ad_name = models.CharField(max_length=250)
    campaign = models.ForeignKey(CampaignGoogle, on_delete=models.CASCADE)
    ad_group = models.ForeignKey(AdGroupData, on_delete=models.CASCADE)
    ad_status = models.CharField(max_length=250)
    final_urls = models.CharField(max_length=250)
    description1 = models.CharField(max_length=250)
    description2 = models.CharField(max_length=250)
    ad_type = models.CharField(max_length=250)
    ad_metrics = models.ForeignKey(Metrics, on_delete=models.CASCADE, related_name='ad_metrics')

    def __str__(self):
        return self.ad_name

class Keyword(models.Model):
    resource_name = models.CharField(max_length=250, unique=True)
    keyword_text = models.CharField(max_length=250)
    keyword_match_type = models.CharField(max_length=250)
    campaign = models.ForeignKey(CampaignGoogle, on_delete=models.CASCADE)
    ad_group = models.ForeignKey(AdGroupData, on_delete=models.CASCADE)
    keyword_metrics = models.ForeignKey(Metrics, on_delete=models.CASCADE, related_name='keyword_metrics')

    def __str__(self):
        return self.keyword_text
