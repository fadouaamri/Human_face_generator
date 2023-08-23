from flask import Flask,render_template,request,redirect
import io
from PIL import Image
import tensorflow
import keras
from keras import load_model
#Create an object of the Flask class
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return
        # get the file uploaded from the fronted
        file = request.files["file"]

        # get the file extention
        file_extension = file.filename.rsplit('.', 1)[1].lower()

        if file_extension == 'jpg':
            img_bytes = file.read()
            img = Image.open(io.BytesIO(img_bytes))
            results = model(img)

    return render_template('index.html')

if __name__=="__main__":
    #use the trained model
    model = load_model('face_gen.h5')

    #run the app
    app.run(debug=True)  # debug=True causes Restarting with stat