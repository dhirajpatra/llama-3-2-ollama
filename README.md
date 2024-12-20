# llama-stack-app

## Overview

`llama-stack-app` is a Docker Compose-based template for developing applications using the Llama model using ollama. This setup allows for rapid prototyping and deployment of applications such as conversational bots or copilots, with built-in support for Retrieval-Augmented Generation (RAG).

The 3B model outperforms the Gemma 2 2.6B and Phi 3.5-mini models on tasks such as:

Following instructions
Summarization
Prompt rewriting
Tool use

Supported Languages: English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai are officially supported. Llama 3.2 has been trained on a broader collection of languages than these 8 supported languages.

This template currently uses the **Llama 3.2 - 1B** model by default, but other models can be integrated as required.

You can use any of the model as per your system and requirement from **https://ollama.com/library/llama3.2/tags**

---

## Branches

This repository has three different branches main, chain and vision. 

- Main is the simplisting form of Chatbot which you can start to translate or other kind of chat.
- Chain is conversational AI bot with LangChain. You can add with RAG process easily. 
- Vision is for chat about the image you uploaded into the chat.

---

## Features
- **RAG Provision**: Prepared to extend with RAG capabilities to enhance answer accuracy and relevance by combining model outputs with external document retrieval.
- **Scalable Architecture**: Uses Docker Compose for scalable and isolated development.
  
---

## Prerequisites
Ensure that you have the following installed:
- Docker
- Docker Compose

---

## How to Run
Clone the repository, navigate to the directory, and run:

```bash
docker-compose up --build --remove-orphans
```

To keep your Docker space clean in local can use the below command
```bash
docker images -f dangling=true | awk '{print $3}' | xargs docker image rm
```

This command will build and run all required services defined in the Docker Compose file. First time it may take several minutes depends on the system and internet speed. As it will pull down the llama model and then can start the service.

---

## Configuration
You can configure the model and server settings in the `llama_config.yaml` file. Example settings include:

```yaml
# Configuration for running Llama model
model:
  type: llama
  parameters:
    model_name: meta-llama/Llama3.2-1B-Instruct:int4-qlora-eo8  # Recommended model for low memory usage
    temperature: 0.7
    max_length: 2048
server:
  host: "0.0.0.0"
  port: 5000
```

---

## References

- [Llama 3.2 Model Library](https://ollama.com/library/llama3.2:1b)

- ![Llama 3.2 chat](images/1.png)
- ![Model info](images/2.png)
- ![Pulling and starting Llama 3.2 model based server](images/3.png)
- ![Llama 3.2 Chat](images/4.png)
- ![Llama 3.2 Hindi Chat](images/5.png)
- ![Llama 3.2 Hindi Translation Chat](images/6.png)
- ![Llama 3.2 Hindi Translation Chat](images/7.png)
- ![Llama 3.2 Python REST Server Structure Chat](images/8.png)
- ![Llama 3.2 Python REST Server Structure Chat](images/9.png)
- ![Llama 3.2 Python REST Server Structure Chat](images/10.png)
- ![Llama 3.2 Hindi to English Google Translation](images/11.png)
- ![Llama 3.2 Hindi to English This Chatbot Translation](images/12.png)
---

## Contributing
We welcome contributions! Please feel free to open issues, suggest features, or submit pull requests to help us improve `llama-stack-app`. To get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch-name`)
3. Commit your changes
4. Push to the branch (`git push origin feature-branch-name`)
5. Open a Pull Request

For larger changes, please open an issue to discuss your proposal first.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

LLAMA 3.2 COMMUNITY LICENSE AGREEMENT
Llama 3.2 Version Release Date: September 25, 2024

“Agreement” means the terms and conditions for use, reproduction, distribution and modification of the Llama Materials set forth herein.

“Documentation” means the specifications, manuals and documentation accompanying Llama 3.2 distributed by Meta at https://llama.meta.com/doc/overview.

https://ollama.com/blog/llama3.2

https://www.promptingguide.ai/

