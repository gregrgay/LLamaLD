# This file contains some useful commands and test locations
# when using LLamaLD. It can be safely deleted once you've learned 
# the commands and locations (also repeated in the README file)

#Clone LLamaLD long description widget from Github
>git clone https://github.com/gregrgay/LLamaLD

#Activate with conda from within the LLamaLD directory
>conda activate llama 

#Run one of the LLama server configurations with incrementally larger language models:

#Smallest LLM
>python -m llama_cpp.server --model models/ggml-model-q4_k.gguf --clip_model_path models/mmproj-model-f16.gguf --chat_format llava-1-5 --n_gpu_layers 1 --n_threads 8
#Small LLM
>python -m llama_cpp.server --model models/ggml-model-q5_k.gguf --clip_model_path models/mmproj-model-f16.gguf --chat_format llava-1-5 --n_gpu_layers 1 --n_threads 8
#Larger LLM
>python -m llama_cpp.server --model models/ggml-model-f16.gguf --clip_model_path models/mmproj-model-f16.gguf --chat_format llava-1-5 --n_gpu_layers 1 --n_threads 8

#Test the LLama server
Go to: http://localhost:8000/docs

#Start LLamaLD widget
>python start.py
Go to: http://localhost:5000

#Try the demo
Go to: http://localhost/widget_test.html