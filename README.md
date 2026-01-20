# hs-code-nlp-classifier-cl
NLP and ML experiments for HS code classification in Chile, including data exploration, preprocessing, and multi-class models such as SVM and BERT.


## Autores

Manuel Bórquez Basáez

https://github.com/mborquezb/

## Arquitectura

```text
    Entrada: descripción del producto
                ↓
[Filtro IN/OUT — BERT binario compartido]
                ↓ 
   ┌───────────────────────────────┐
   ↓                               ↓
[SVM multiclase]           [BERT multiclase] 
        ↓                          ↓
   Código HS                  Código HS
        ↓                          ↓
            [Revisión Expeta]
```

### Filtro IN/OUT

Para el filtro IN/OUT basado en BERT se aplica únicamente una normalización mínima del texto. No se realiza eliminación de stopwords, stemming ni lematización, preservando la señal semántica completa, en consistencia con el preentrenamiento del modelo.

## Setup

### conda environment setup

```bash
# definición de entorno conda
conda env create -f environment.yml

# activación del entorno
conda activate mbb-cc66r-1-prj

# registro del kernel
python -m ipykernel install --user --name mbb-cc66r-1-prj --display-name "Python (mbb-cc66r-1-prj)"

# actualizar el entorno
conda env update --file environment.yml --prune 

# reinicio / limpieza
conda deactivate
conda clean --all --yes
conda remove -n mbb-cc66r-1-prj --all

```

### gpu

```bash
# verificación de acceso a GPU integrada al mac
python -c "import torch; print('PyTorch:', torch.__version__); print('Torchvision:', __import__('torchvision').__version__); print('MPS available:', torch.backends.mps.is_available())"
```
