# AI Long Description Generator README

This utility is used to scan webpages for images and add a long description widget. Clicking the widget at the bottom right of an image opens a dialog with the URL to the image in a text field, and a default prompt "Describe this image." The form data is submitted to a local Llamma AI. Local images can also be dragged onto drop area to have that image described. 

Assumptions:
- A Linux (preferred), or Mac, or Windows OS with Python 3.8+ available
- A C compiler 
- A functioning LLmama server. See [llama.cpp on Github](https://github.com/ggerganov/llama.cpp))
- A LLM downloaded from Hugging Face (one ggml and one)

LLama Documentation
[Installing LLama](https://llama-cpp-python.readthedocs.io/en/stable/#installation)

##Install LLamma
Assuming a functional Python environment, run pip to install LLamma. Note the various configuration and environement variable to set depending on the OS, in the documentation above
>pip install llama-cpp-python



##Download Large Language Models (LLMs)
There aren a variety of LLMs to choose from. If your running LLama on the personal computer, start with the smallest one (~4.1GB) and if it runs without too much delay, try one of the larger LLMs. LLMs can be found throguh Hugging Face. You'll need one GGML and one MMProj model.

###Hugging Face Downloads
https://huggingface.co/mys/ggml_llava-v1.5-7b/tree/main

##Activate the LLamma environment
From within the llava-openai-server directory start llama by running:
>conda activate llama 

Start the Lamma server
In the same directory, now with an active LLama environment, run:
>python -m llama_cpp.server --model llava/ggml-model-q4_k.gguf --clip_model_path llava/mmproj-model-f16.gguf --chat_format llava-1-5 --n_gpu_layers 1 --n_threads 8

[Note: ]