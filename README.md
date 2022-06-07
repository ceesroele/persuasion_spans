<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Detecting Persuasion with spaCy

Configuration and code accompanying _[Detecting Persuasion with spaCy](https://cees-roele.medium.com/detecting-persuasion-with-spacy-6b6beba51076)_.

_Persuasion techniques_ express shortcuts in the argumentation process, e.g. by leveraging on the _emotions_ of the audience or by using _logical fallacies_ to influence it. This project creates a spaCy pipeline with a `SpanCategorizer` to detect and classify spans in which persuasion techniques are used in a text.
 
 Notes:
 * No other pre-processing of data is performed except conversion to `spacy` binary format.
 * Default configuration files are used for _small_, _large_, and _transformer_ models.
 * After training/evaluation of every model, **the created model is removed**! For the purpose of the associated article, we are interested in the metrics, not the created models.
 * For the article describing this project, `suggester` configuration is changed manually to vary between maximum 16-grams and maximum 32-grams configurations.
 * Evaluation output for training different models (JSON format) is processed by `report.py` to allow for comparison.
 * GPU is used only for the transformer models.
 * A `suggester` configuration for maximum 32-grams with a **transformer** model will run out of 8GB memory of a GPU. In the provided configuration here batch sizes are tweaked to make it run, but at a loss of some twenty percent of accuracy. * On a 6-core CPU, a 32-grams configuration with a transformer model took some 14 hours to run!
 
 Python code is used to:
 * create the corpus in `spacy` format from the original dataset.
 * extract data from generated metrics files for reporting.
 

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `corpus` | Convert the data to spaCy's format |
| `train_sm` | Train and evaluate 'sm' model for 16-grams and 32-grams configurations |
| `train_lg` | Train and evaluate 'lg' model for 16-grams and 32-grams configurations |
| `train_trf` | Train and evaluate 'trf' model for 16-grams and 32-grams configurations |
| `report` | Convert metrics of the different trained models to CSV for reading into notebook |
| `clean` | Remove intermediate files |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `corpus` &rarr; `train_sm` &rarr; `train_lg` &rarr; `train_trf` &rarr; `report` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets` | Git | Dev dataset from SemEval2021 Task-6 'Detection of Persuasive Techniques in Texts and Images' |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->