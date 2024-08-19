from django.contrib import admin

from .models.googleanalytics_models import *
from .models.google_models import *

googleanalytics_modals = [
    GoogleAnalyticsProperty, UserMetrics, SessionMetrics, EventMetrics, EcommerceMetrics, EngagementMetrics, AdMetrics, LifetimeValueMetrics, DemographicMetrics, TechnologyMetrics, GoalMetrics, ContentMetrics, UTMParamsMetrics, RealtimeMetrics, PovitMetrics
]

google_modals = [
    CampaignTargetCpa,  CampaignBudgetDetails, CampaignGroup, CampaignMetrics, CampaignGoogle, AdGroupMetrics, AdGroupData, Metrics, AdData, Keyword
]

for modal in googleanalytics_modals:
    admin.site.register(modal)

for modal in google_modals:
    admin.site.register(modal)