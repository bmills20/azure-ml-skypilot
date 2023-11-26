# Deploying a HuggingFace model to Azure Machine learning (SkyPilot + vLLM + Azure CLI)

This repository contains the necessary configuration and code to deploy a Hugging Face model to Azure using SkyPilot.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Azure CLI: Installed the Azure Command Line Interface (CLI). Installation guide available [here](https://docs.microsoft.com/cli/azure/install-azure-cli).
- SkyPilot: Install SkyPilot following the instructions on their [official installation page](https://skypilot.readthedocs.io/en/latest/getting-started/installation.html). SkyPilot is essential for deploying and managing your model on Azure.

- You have a `.env` file in your repository root with your Azure credentials and other necessary environment variables.
- You have installed the necessary Python packages. You can do this by running `pip install -r requirements.txt` in your repository root.

## Deploying the Model

To deploy the model to Azure, run the following command:

```
sky launch -c vllm-serve -s serve.yaml
```

This deploys your specified model to a cluster named `vllm-serve`

More info about how SkyPilot works with vLLM [here](https://github.com/skypilot-org/skypilot/blob/master/llm/vllm/README.md).
