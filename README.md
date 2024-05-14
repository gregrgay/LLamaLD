# LLama AI Long Description Generator README

This utility is used to scan a webpage for images and add a long description widget. Clicking the widget at the bottom right of an image opens a dialog with the URL to the image in a text field, and a default prompt "Describe this image" that can be customized to adjust the description output.  The form data is submitted to a local LLama AI server (or external GPT4 server). Local images can also be dragged onto the drop area to have them described. 

## Some Assumptions:
- A Linux (preferred), or Mac, or Windows OS with Python 3.8+ available
- A C compiler 
- [Anaconda python development environment](https://www.anaconda.com/download)  or use [miniconda for Mac](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html)
- A functioning LLmama server. Installed as a Python package, or from a Github repository See [llama.cpp on Github](https://github.com/ggerganov/llama.cpp)
- Large Language Models (LLMs) downloaded from Hugging Face 

## LLama Documentation
- [Installing LLama](https://llama-cpp-python.readthedocs.io/en/stable/#installation)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/introduction) for settings that can be customized.

### Install LLama
Assuming an up to date Python environment, run pip to install LLama.cpp. Note the various configuration and environment variables that may need to be set depending on the OS, in the documentation above. 
>pip install llama-cpp-python

Or, for the absolute latest LLama code, it can be cloned from Github
>git clone https://github.com/abetlen/llama-cpp-python.git

NOTE: Depending on the python environment, you may need to install other python modules (e.g. flask, openai, base64). Watch the error messages if generated, to determine which modules need to be installed, and install them using pip (e.g. 'pip install flask').

### Clone LLamaLD into a working directory, I use one called AI/
>cd AI

>git clone https://github.com/gregrgay/LLamaLD

Or, clone the LLamaLD repository into you own account and clone it instead, for more control over the files if you wish to customize the tool and track your work.
>git clone https://github.com/my_git_account/LLamaLD

### Download Large Language Models (LLMs)
There are a variety of LLMs to choose from. If you're running LLama on the personal computer, start with the smallest one (~4.1GB) and if it runs without too much delay, try one of the larger LLMs. LLMs can be found through Hugging Face. You'll need one GGML and one MMProj model.

#### Hugging Face Downloads
https://huggingface.co/mys/ggml_llava-v1.5-7b/tree/main
- [ggml-model-q4_k.gguf](https://huggingface.co/mys/ggml_llava-v1.5-7b/resolve/main/ggml-model-q4_k.gguf?download=true) (4.08GB) 
- [mmproj-model-f16.gguf](https://huggingface.co/mys/ggml_llava-v1.5-7b/resolve/main/mmproj-model-f16.gguf?download=true) (624MB)

Once downloaded move the models into  the models directory
>mv ggml-model-q4_k.gguf AI/LLamaLD/models/

>mv mmproj-model-f16.gguf AI/LLamaLD/models/

### Activate the LLama environment
From within the LLamaLD directory activate llama by running:
>cd AI/LLamaLD

>conda activate llama 

### Start the LLama server
In the LLamaLD, now with an active LLama environment, start the lamma.cpp server. Note the --model and --clip_model_path:
>cd AI/LLamaLD 

>python -m llama_cpp.server --model models/ggml-model-q4_k.gguf --clip_model_path models/mmproj-model-f16.gguf --chat_format llava-1-5 --n_gpu_layers 1 --n_threads 8

If successful, you should be able to open the LLama server in a web browser by pointing it to:
>http://localhost:8000/docs

NOTE: again watch for error message and install any missing python packages the errors mention.

## Run LLamaLD
With the LLama server running on port :8000, start the LLamaLD server
>python start.py

The widget then becomes available on port :5000
>http://localhost:5000


## Try the Demo
Open the demo page at:
>http://localhost/widget_test.html

 Then click the icon at the bottom right of each image. In the dialog that opens, press the Submit button to send the default data in the form to the LLama server. Or, customize the prompt to control what gets described. Or, drag a local image on to the drop area, then press submit to describe that image instead of the default image from which the widget was opened. 






