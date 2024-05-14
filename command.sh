#Clone llama_cpp.server


#Run with conda
#conda create -n llama python=3.10.13 (if not already set)
>conda activate llama (to start lmama server)

#llama version
>python -m llama_cpp.server --model llava/ggml-model-q4_k.gguf --clip_model_path llava/mmproj-model-f16.gguf --chat_format llava-1-5 --n_gpu_layers 1 --n_threads 8
>python -m llama_cpp.server --model llava/ggml-model-q5_k.gguf --clip_model_path llava/mmproj-model-f16.gguf --chat_format llava-1-5 --n_gpu_layers 1 --n_threads 8
>python -m llama_cpp.server --model llava/ggml-model-f16.gguf --clip_model_path llava/mmproj-model-f16.gguf --chat_format llava-1-5 --n_gpu_layers 1 --n_threads 8
Test server
 http://localhost:8000/doc

#Start lava widget
>python start.py

LLava version

python -m llava.serve.cli \
    --model-path liuhaotian/llava-v1.5-7b \
    --image-file "https://llava-vl.github.io/static/images/view.jpg" \
    --device mps
python -m llava.serve.cli \
    --model-path liuhaotian/llava-v1.5-7b \
    --image-file "https://llava-vl.github.io/static/images/view.jpg" \
    --device mps