import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-for-testing-only')
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    
    # LLM settings
    DEFAULT_MODEL = "gemini-pro"
    TEMPERATURE = 0.7
    MAX_TOKENS = 500
    
    # Product description templates
    TEMPLATES = {
        'default': """Create a compelling product description for a {category} product named "{product_name}". 
                   Materials: {materials}. Key features: {features}. Main benefits: {benefits}. 
                   Target audience: {target_audience}. Additional info: {additional_info}.""",
        
        'promotional': """Create an enthusiastic promotional product description for a {category} product named "{product_name}" 
                        that will excite customers to make a purchase. Materials: {materials}. 
                        Key features: {features}. Main benefits: {benefits}. Target audience: {target_audience}. 
                        Additional info: {additional_info}. Include emojis and excitement.""",
        
        'technical': """Create a detailed technical product description for a {category} product named "{product_name}" 
                      that focuses on specifications and features. Materials: {materials}. 
                      Key features: {features}. Main benefits: {benefits}. Target audience: {target_audience}. 
                      Additional info: {additional_info}. Format with bullet points for features.""",
        
        'minimalist': """Create a short, concise product description for a {category} product named "{product_name}" 
                       using as few words as possible while still being effective. Materials: {materials}. 
                       Key features: {features}. Main benefits: {benefits}. Target audience: {target_audience}.
                       Additional info: {additional_info}."""
    }