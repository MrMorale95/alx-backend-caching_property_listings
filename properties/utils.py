from django.core.cache import cache
from .models import Property

def get_all_properties():
    # Try to get cached queryset
    properties = cache.get('all_properties')
    
    if not properties:
        # If not cached, query the database
        properties = list(Property.objects.all())  # convert to list for caching
        # Store in Redis for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)
    
    return properties
