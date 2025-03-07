from flask import Flask, render_template, request, jsonify
from app.llm_service import LLMService

app = Flask(__name__)
llm_service = LLMService()

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Generate a product description."""
    try:
        # Get form data
        product_data = {
            'category': request.form.get('category', ''),
            'product_name': request.form.get('product_name', ''),
            'materials': request.form.get('materials', ''),
            'features': request.form.get('features', ''),
            'benefits': request.form.get('benefits', ''),
            'target_audience': request.form.get('target_audience', ''),
            'additional_info': request.form.get('additional_info', '')
        }
        
        # Validate required fields
        if not product_data['product_name'] or not product_data['category']:
            return jsonify({'error': 'Product name and category are required'}), 400
        
        # Get template type
        template_name = request.form.get('template', 'default')
        
        # Generate description
        description = llm_service.generate_description(product_data, template_name)
        
        return jsonify({'description': description})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)