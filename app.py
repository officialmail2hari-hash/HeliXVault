from flask import Flask,render_template,request,jsonify
from modules.compressor import compress_data,decompress_data,compression_statistics
from modules.binary_converter import bytes_to_binary,binary_to_bytes,binary_statistics
from modules.dna_encoder import binary_to_dna,dna_statistics
from modules.dna_decoder import dna_to_binary
from modules.analyser import analyse_dna
from modules.verifier import verify_data

app=Flask(__name__)
app.config["MAX_CONTENT_LENGTH"]=10*1024*1024

@app.route("/")
def home(): return render_template("index.html")

@app.post("/api/encode")
def encode():
    f=request.files.get("file")
    if not f or not f.filename: return jsonify(error="Please choose a file."),400
    try:
        raw=f.read()
        compressed=compress_data(raw)
        binary=bytes_to_binary(compressed)
        dna=binary_to_dna(binary)
        recovered_binary=dna_to_binary(dna)
        recovered_compressed=binary_to_bytes(recovered_binary)
        recovered=decompress_data(recovered_compressed)
        return jsonify(success=True,
            file={"name":f.filename,"type":f.mimetype or "Unknown","size_bytes":len(raw)},
            compression=compression_statistics(raw,compressed),
            binary={**binary_statistics(binary),"preview":binary[:256]},
            dna={**dna_statistics(dna),"preview":dna[:500]},
            analysis=analyse_dna(dna),
            verification=verify_data(raw,recovered),
            mapping={"00":"A","01":"C","10":"G","11":"T"},
            note="Computational demonstration only; laboratory synthesis/sequencing is separate.")
    except Exception as e: return jsonify(error=str(e)),400

@app.route("/physical-dna")
def physical(): return render_template("physical.html")

if __name__=="__main__": app.run(debug=True)
