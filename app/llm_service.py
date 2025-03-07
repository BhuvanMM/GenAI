import google.generativeai as genai
from config.config import Config

class LLMService:
    """Service for generating product descriptions using Gemini API."""
    
    def __init__(self):
        # Configure the Gemini API
        genai.configure(api_key=Config.GEMINI_API_KEY)
        
        # Change to a simpler model - typically 'gemini-1.0-pro' or 'gemini-1.5-flash'
        # would be simpler options than larger variants
        self.model = "gemini-1.5-flash"  # Using a simpler model version
        self.temperature = 0.7  # Default temperature
        self.max_tokens = 256  # Reduced token limit for simpler responses
        self.templates = Config.TEMPLATES
    
    def generate_description(self, product_data, template_name='default'):
        """Generate a product description based on the provided data and template."""
        if template_name not in self.templates:
            template_name = 'default'
            
        # Prepare the template with product data
        prompt = self.templates[template_name].format(
            category=product_data.get('category', ''),
            product_name=product_data.get('product_name', ''),
            materials=product_data.get('materials', 'N/A'),
            features=product_data.get('features', 'N/A'),
            benefits=product_data.get('benefits', 'N/A'),
            target_audience=product_data.get('target_audience', 'general consumers'),
            additional_info=product_data.get('additional_info', '')
        )
        
        try:
            # Initialize the basic Gemini model
            model = genai.GenerativeModel(
                model_name=self.model,
                generation_config={
                    "temperature": self.temperature,
                    "max_output_tokens": self.max_tokens,
                }
            )
            
            # Simplify to a single prompt instead of chat
            response = model.generate_content(prompt)
            
            # Extract and return the generated description
            return response.text.strip()
            
        except Exception as e:
            print(f"Error generating description: {e}")
            return "Error generating product description. Please try again."