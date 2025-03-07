document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generateBtn');
    const copyBtn = document.getElementById('copyBtn');
    const productForm = document.getElementById('productForm');
    const outputContainer = document.getElementById('output');
    const descriptionOutput = document.getElementById('descriptionOutput');
    const loader = document.getElementById('loader');
    
    // Generate button click handler
    generateBtn.addEventListener('click', function() {
        // Check required fields
        const productName = document.getElementById('product_name').value;
        const category = document.getElementById('category').value;
        
        if (!productName || !category) {
            alert('Please fill in the required fields (Product Name and Category)');
            return;
        }
        
        // Show loader
        loader.style.display = 'block';
        
        // Prepare form data
        const formData = new FormData(productForm);
        
        // Send request to the server
        fetch('/generate', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Server error');
            }
            return response.json();
        })
        .then(data => {
            // Hide loader
            loader.style.display = 'none';
            
            // Display the result
            if (data.error) {
                descriptionOutput.textContent = `Error: ${data.error}`;
            } else {
                descriptionOutput.textContent = data.description;
                outputContainer.style.display = 'block';
            }
        })
        .catch(error => {
            // Hide loader
            loader.style.display = 'none';
            
            // Show error
            alert('An error occurred. Please try again.');
            console.error('Error:', error);
        });
    });
    
    // Copy button functionality
    copyBtn.addEventListener('click', function() {
        const descriptionText = descriptionOutput.textContent;
        
        navigator.clipboard.writeText(descriptionText)
            .then(() => {
                const originalText = copyBtn.textContent;
                copyBtn.textContent = "Copied!";
                setTimeout(() => {
                    copyBtn.textContent = originalText;
                }, 2000);
            })
            .catch(err => {
                console.error('Failed to copy text: ', err);
                alert('Failed to copy to clipboard. Please try selecting and copying the text manually.');
            });
    });
});