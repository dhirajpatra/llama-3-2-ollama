# llama-stack-app

## Overview

`llama-stack-app` is a Docker Compose-based template for developing applications using the Llama model. This setup allows for rapid prototyping and deployment of applications such as conversational bots or copilots, with built-in support for Retrieval-Augmented Generation (RAG).

This template currently uses the **Llama 3.2 - 1B** model by default, but other models can be integrated as required.

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

- ![Llama 3.2 chat](1.jpg)
- ![Model info](2.jpg)
- ![Pulling and starting Llama 3.2 model based server](3.jpg)
- ![Llama 3.2 Chat](4.jpg)

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
