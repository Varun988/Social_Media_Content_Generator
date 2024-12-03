import tweepy
import os

def post_to_social_media(content, platform_choice):
    """Post content to the selected social media platform."""
    if platform_choice.lower() == 'twitter':
        return post_to_twitter(content)
    elif platform_choice.lower() == 'facebook':
        return post_to_facebook(content)
    elif platform_choice.lower() == 'instagram':
        return post_to_instagram(content)
    else:
        raise ValueError(f"Unsupported platform: {platform_choice}")

def post_to_twitter(content):
    """Post content to Twitter using Tweepy."""
    print("Posting to Twitter...")
    
    # Twitter API credentials (replace with your own)
    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    
    # Authenticate to Twitter
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    
    # Post content
    api.update_status(content)
    return f"Content posted to Twitter: {content}"

def post_to_facebook(content):
    """Post content to Facebook using an API (Placeholder)."""
    print("Posting to Facebook...")
    # Simulate posting to Facebook (replace with actual API)
    return f"Content posted to Facebook: {content}"

def post_to_instagram(content):
    """Post content to Instagram (Placeholder)."""
    print("Posting to Instagram...")
    # Simulate posting to Instagram (replace with actual API)
    return f"Content posted to Instagram: {content}"
