# Translation settings
TRANSLATION_CACHE_ENABLED = True
TRANSLATION_CACHE_TIMEOUT = 3600  # Cache duration in seconds

# Supported languages for the project
LANGUAGES = [
    ('en', 'English'),
    ('zh-CN', 'Chinese (Simplified)'),
    ('fr', 'French'),
    ('de', 'German'),
    ('es', 'Spanish'),
]

# Middleware settings, including locale middleware to support language selection
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Allows automatic language switching based on user preference
    # Other middleware...
]

# Default language setting
LANGUAGE_CODE = 'en'

# Enable Django's internationalization and localization features
USE_I18N = True
USE_L10N = True

# Time zone settings
TIME_ZONE = 'UTC'
USE_TZ = True

# Translation cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',  # Choose the appropriate cache location
    },
    'translation_cache': {  # Cache configuration specifically for translations
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': TRANSLATION_CACHE_TIMEOUT,  # Cache timeout duration
    },
}

# Googletrans configuration (assuming usage of Googletrans API)
GOOGLETRANSLATE_API_KEY = 'your-google-translate-api-key'  # Replace with the actual API key

# Translation error handling message
TRANSLATION_ERROR_MESSAGE = "Translation is not available at the moment. Please try again later."

# Custom translation function example
def translate_text(text, src_language, dest_language):
    """
    Uses googletrans library for translation and caches the translation result.
    """
    if TRANSLATION_CACHE_ENABLED:
        # Try retrieving translation from cache
        cache_key = f'translation_{src_language}_{dest_language}_{text}'
        translation = cache.get(cache_key)
        
        if translation is not None:
            return translation
    
    try:
        from googletrans import Translator
        translator = Translator()
        translation = translator.translate(text, src=src_language, dest=dest_language).text
        
        if TRANSLATION_CACHE_ENABLED:
            # Store translation result in cache
            cache.set(cache_key, translation, TRANSLATION_CACHE_TIMEOUT)
        
        return translation
    except Exception as e:
        # Catch any translation errors and return a friendly message
        print(f"Translation error: {e}")
        return TRANSLATION_ERROR_MESSAGE
