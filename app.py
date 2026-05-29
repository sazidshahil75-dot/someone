from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get list of images from the images folder
    images_dir = os.path.join(app.static_folder, 'images')
    images = []
    if os.path.exists(images_dir):
        for f in os.listdir(images_dir):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                images.append(f'/static/images/{f}')
    return render_template('index.html', images=images)

@app.route('/get-images')
def get_images():
    images_dir = os.path.join(app.static_folder, 'images')
    images = []
    if os.path.exists(images_dir):
        for f in os.listdir(images_dir):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                images.append(f'/static/images/{f}')
    return jsonify(images)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
