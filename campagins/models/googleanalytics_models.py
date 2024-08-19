from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class GoogleAnalyticsProperty(TimeStampedModel):
    INDUSTRY_CHOICES = [
        ('Ecommerce', 'Ecommerce'),
        ('SaaS', 'SaaS'),
        ('Education', 'Education'),
    ]

    SERVICE_LEVEL_CHOICES = [
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]

    channel_type = models.CharField(max_length=255)
    property_id = models.CharField(max_length=255, unique=True)
    property_details = models.TextField()
    parent = models.CharField(max_length=255, null=True, blank=True)
    display_name = models.CharField(max_length=255)
    industry_category = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    time_zone = models.CharField(max_length=255)
    currency_code = models.CharField(max_length=10)
    service_level = models.CharField(max_length=50, choices=SERVICE_LEVEL_CHOICES)
    account_id = models.CharField(max_length=255)

    class Meta:
        indexes = [
            models.Index(fields=['property_id']),
        ]

class UserMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='user_metrics')
    active_users = models.PositiveIntegerField()
    new_users = models.PositiveIntegerField()
    total_users = models.PositiveIntegerField()
    crash_free_users_rate = models.DecimalField(max_digits=5, decimal_places=2)
    crash_affected_users = models.PositiveIntegerField()
    user_engagement_duration = models.PositiveIntegerField()
    user_stickiness = models.DecimalField(max_digits=5, decimal_places=2)
    user_retention = models.DecimalField(max_digits=5, decimal_places=2)

class SessionMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='session_metrics')
    sessions = models.PositiveIntegerField()
    engaged_sessions = models.PositiveIntegerField()
    sessions_per_user = models.DecimalField(max_digits=5, decimal_places=2)
    average_session_duration = models.DecimalField(max_digits=10, decimal_places=2)
    bounce_rate = models.DecimalField(max_digits=5, decimal_places=2)
    engagement_rate = models.DecimalField(max_digits=5, decimal_places=2)
    session_duration_per_user = models.DecimalField(max_digits=10, decimal_places=2)

class EventMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='event_metrics')
    event_count = models.PositiveIntegerField()
    event_value = models.DecimalField(max_digits=20, decimal_places=2)
    event_count_per_user = models.DecimalField(max_digits=10, decimal_places=2)
    events_per_session = models.DecimalField(max_digits=10, decimal_places=2)

class EcommerceMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='ecommerce_metrics')
    purchase_revenue = models.DecimalField(max_digits=20, decimal_places=2)
    transactions = models.PositiveIntegerField()
    purchase_rate = models.DecimalField(max_digits=5, decimal_places=2)
    average_purchase_revenue = models.DecimalField(max_digits=20, decimal_places=2)
    refund_amount = models.DecimalField(max_digits=20, decimal_places=2)
    average_purchase_value = models.DecimalField(max_digits=20, decimal_places=2)
    ecommerce_purchases = models.PositiveIntegerField()

class EngagementMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='engagement_metrics')
    average_session_duration = models.DecimalField(max_digits=10, decimal_places=2)
    bounce_rate = models.DecimalField(max_digits=5, decimal_places=2)
    engagement_rate = models.DecimalField(max_digits=5, decimal_places=2)
    screen_page_views = models.PositiveIntegerField()
    engaged_sessions_per_user = models.DecimalField(max_digits=5, decimal_places=2)
    user_engagement_duration = models.PositiveIntegerField()
    screen_page_views_per_session = models.DecimalField(max_digits=5, decimal_places=2)

class AdMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='ad_metrics')
    ad_clicks = models.PositiveIntegerField()
    ad_cost = models.DecimalField(max_digits=20, decimal_places=2)
    ad_impressions = models.PositiveIntegerField()
    ad_revenue = models.DecimalField(max_digits=20, decimal_places=2)
    return_on_ad_spend = models.DecimalField(max_digits=5, decimal_places=2)
    ad_cost_per_click = models.DecimalField(max_digits=10, decimal_places=2)
    ad_click_through_rate = models.DecimalField(max_digits=5, decimal_places=2)

class LifetimeValueMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='lifetime_value_metrics')
    lifetime_value_revenue = models.DecimalField(max_digits=20, decimal_places=2)
    lifetime_value_purchases = models.PositiveIntegerField()
    average_lifetime_value = models.DecimalField(max_digits=20, decimal_places=2)
    customer_lifetime_value = models.DecimalField(max_digits=20, decimal_places=2)

class DemographicMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='demographic_metrics')
    country = models.CharField(max_length=255)
    date = models.DateField()
    device_category = models.CharField(max_length=255)
    operating_system = models.CharField(max_length=255)
    browser = models.CharField(max_length=255)
    screen_resolution = models.CharField(max_length=255)
    app_version = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)

class TechnologyMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='technology_metrics')
    device_category = models.CharField(max_length=255)
    operating_system = models.CharField(max_length=255)
    browser = models.CharField(max_length=255)
    screen_resolution = models.CharField(max_length=255)
    app_version = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)

class GoalMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='goal_metrics')
    goal_completions_all = models.PositiveIntegerField()
    goal_conversion_rate_all = models.DecimalField(max_digits=5, decimal_places=2)
    goal_value_all = models.DecimalField(max_digits=20, decimal_places=2)
    goal_starts_all = models.PositiveIntegerField()

class ContentMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='content_metrics')
    page_views = models.PositiveIntegerField()
    unique_page_views = models.PositiveIntegerField()
    time_on_page = models.DecimalField(max_digits=10, decimal_places=2)
    entrances = models.PositiveIntegerField()
    page_value = models.DecimalField(max_digits=20, decimal_places=2)
    exit_rate = models.DecimalField(max_digits=5, decimal_places=2)

class UTMParamsMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='utm_params_metrics')
    date = models.DateField()
    source = models.CharField(max_length=255)
    medium = models.CharField(max_length=255)
    campaign = models.CharField(max_length=255)
    term = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    sessions = models.PositiveIntegerField()
    users = models.PositiveIntegerField()
    page_views = models.PositiveIntegerField()

class RealtimeMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='realtime_metrics')
    country = models.CharField(max_length=255)
    active_users = models.PositiveIntegerField()
    screen_page_views = models.PositiveIntegerField()

class PovitMetrics(TimeStampedModel):
    property = models.ForeignKey(GoogleAnalyticsProperty, on_delete=models.CASCADE, related_name='povit_metrics')
    sessions = models.CharField(max_length=255)
    date = models.DateField()
    country = models.CharField(max_length=255)
