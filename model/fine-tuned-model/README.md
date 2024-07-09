---
base_model: sentence-transformers/all-MiniLM-L6-v2
datasets: []
language: []
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:14
- loss:SoftmaxLoss
widget:
- source_sentence: 'Q2a: Is escrow amount grete then the Retention Amount ?'
  sentences:
  - 'A4: No, as the signing and closing are simultaneous.'
  - 'A6: Yes (See Section 2.07)'
  - 'A2a: No. '
- source_sentence: "\tQ3a: May the Escrow Amount serve as a recourse for the Buyer\
    \ in case of breach of representations by the Company?"
  sentences:
  - 'A2: The escrow amount is equal to $1,000,000.'
  - 'A1:  Except in the case of fraud, the Sellers have no liability for breach of
    representations and warranties (See section 10.01)'
  - "\tA3a: No"
- source_sentence: 'Q1a: Would the Sellers be responsible if after the closing it
    is determined that there were inaccuracies in the representation provided by them
    where such inaccuracies are the resolute of the Sellers’ gross negligence? '
  sentences:
  - a
  - "\tA10a: No. If the assignment is not part of a sale of all or substantially all\
    \ of the Buyer’s assets, the assignment requires the consent of the Company and\
    \ the Seller’s Representative. "
  - 'A10: If the assignment is to an Affiliate or purchaser of all of the Buyer’s
    assets, no consent is required. Otherwise, the consent of the Company and the
    Seller Representative is required. '
- source_sentence: 'Q7: Does the Buyer need to pay the Employees Closing Bonus Amount
    directly to the Company’s employees?'
  sentences:
  - 'A9: No. '
  - 'A7: No. (See Section 2.10)  '
  - 'A5: Yes. (See defining of Sellers Transaction Expenses).'
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision 8b3219a92973c328a8e22fadcfa821b5dc75636a -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 tokens
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'Q7: Does the Buyer need to pay the Employees Closing Bonus Amount directly to the Company’s employees?',
    'A7: No. (See Section 2.10)  ',
    'A9: No. ',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset


* Size: 14 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                         | sentence_1                                                                        | label                        |
  |:--------|:-----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:-----------------------------|
  | type    | string                                                                             | string                                                                            | int                          |
  | details | <ul><li>min: 13 tokens</li><li>mean: 24.14 tokens</li><li>max: 49 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 19.29 tokens</li><li>max: 44 tokens</li></ul> | <ul><li>1: 100.00%</li></ul> |
* Samples:
  | sentence_0                                                                                                                      | sentence_1                                                                                                                                                                                                  | label          |
  |:--------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
  | <code>	Q3a: May the Escrow Amount serve as a recourse for the Buyer in case of breach of representations by the Company?</code> | <code>	A3a: No</code>                                                                                                                                                                                       | <code>1</code> |
  | <code>Q4:  Are there any conditions to the closing?</code>                                                                      | <code>A4: No, as the signing and closing are simultaneous.</code>                                                                                                                                           | <code>1</code> |
  | <code>Q10: Whose consent is required for the assignment of the Agreement by the Buyer? </code>                                  | <code>A10: If the assignment is to an Affiliate or purchaser of all of the Buyer’s assets, no consent is required. Otherwise, the consent of the Company and the Seller Representative is required. </code> | <code>1</code> |
* Loss: [<code>SoftmaxLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#softmaxloss)

### Training Hyperparameters
#### Non-Default Hyperparameters

- `num_train_epochs`: 1
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 8
- `per_device_eval_batch_size`: 8
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 1
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: False
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `dispatch_batches`: None
- `split_batches`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin

</details>

### Framework Versions
- Python: 3.10.12
- Sentence Transformers: 3.0.1
- Transformers: 4.42.3
- PyTorch: 2.3.1+cu121
- Accelerate: 0.32.0
- Datasets: 2.20.0
- Tokenizers: 0.19.1

## Citation

### BibTeX

#### Sentence Transformers and SoftmaxLoss
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->