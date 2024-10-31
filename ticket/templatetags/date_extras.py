from django import template
from datetime import timedelta

register = template.Library()

@register.simple_tag
def calculate_duration(start_date, end_date):
    """
    Calculate the duration between two datetime objects and return as
    'X days, Y hours, Z minutes'.
    """
    if not start_date or not end_date:
        return "Dates invalides"

    # Calculate the time difference
    duration = end_date - start_date

    # Extract days, hours, and minutes from the timedelta
    days = duration.days
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    days = f"{days} jours" if days > 0 else ""
    hours = f"{hours} heures" if hours > 0 else ""
    minutes = f"{minutes} minutes" if minutes > 0 else ""
    seconds = f"{seconds} secondes" if seconds > 0 else ""

    # Format the duration string
    duration_str = f"{days} {hours} {minutes} {seconds}"
    return duration_str
